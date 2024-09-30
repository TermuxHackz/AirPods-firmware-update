_F='purchase_date'
_E='timestamp'
_D=True
_C='case'
_B='right'
_A='left'
import discord
from discord.ext import commands
from discord import app_commands
import json
from datetime import datetime,timedelta
import matplotlib.pyplot as plt,io,os,numpy as np
from utils import format_multi_timezone,format_pacific_time
class AirPodsBatteryTrackerCog(commands.Cog):
	def __init__(A,bot):A.bot=bot;A.battery_log_file='airpods_battery_log.json';A.user_info_file='airpods_user_info.json';A.ensure_files_exist()
	def ensure_files_exist(A):
		for B in[A.battery_log_file,A.user_info_file]:
			if not os.path.exists(B):
				with open(B,'w')as C:json.dump({},C)
	def load_json_file(B,file_name):
		try:
			with open(file_name,'r')as A:return json.load(A)
		except(FileNotFoundError,json.JSONDecodeError):return{}
	def save_json_file(B,data,file_name):
		with open(file_name,'w')as A:json.dump(data,A,indent=2)
	def parse_timestamp(B,timestamp_str):
		A=timestamp_str
		try:return datetime.fromisoformat(A)
		except ValueError:return datetime.strptime(A,'%Y-%m-%d %I:%M:%S %p %Z')
	def load_battery_log(A):return A.load_json_file(A.battery_log_file)
	def save_battery_log(A,data):A.save_json_file(data,A.battery_log_file)
	def estimate_max_capacity(K,battery_logs,purchase_date):
		A=battery_logs
		if not A:return{_A:100,_B:100,_C:100}
		E=(datetime.now()-datetime.fromisoformat(purchase_date)).days;F=min(E/2,500);G=.0004;B=100-F*G*100;H=max(A[_A]for A in A);I=max(A[_B]for A in A);J=max(A[_C]for A in A);C=.7;D=.3;return{_A:C*B+D*H,_B:C*B+D*I,_C:C*B+D*J}
	@app_commands.command(name='log_battery',description='Log the current battery levels of your AirPods')
	@app_commands.describe(left='Battery percentage of left AirPod',right='Battery percentage of right AirPod',case='Battery percentage of AirPods case')
	async def log_battery(self,interaction,left,right,case):
		E=case;D=right;C=left;B=interaction
		if not 0<=C<=100 or not 0<=D<=100 or not 0<=E<=100:await B.response.send_message('Battery percentages must be between 0 and 100.',ephemeral=_D);return
		F=str(B.user.id);G=format_pacific_time();H=format_multi_timezone();A=self.load_battery_log()
		if F not in A:A[F]=[]
		I={_E:G,_A:C,_B:D,_C:E};A[F].append(I);self.save_battery_log(A);await B.response.send_message(f"Battery levels logged at:\n{H}\n Left {C}%, Right {D}%, Case {E}%",ephemeral=_D)
	@app_commands.command(name='set_airpods_info',description='Set your AirPods purchase date and model')
	@app_commands.describe(purchase_date='The date you purchased your AirPods (YYYY-MM-DD)',model="Your AirPods model (e.g., 'AirPods Pro', 'AirPods 2nd Gen')")
	async def set_airpods_info(self,interaction,purchase_date,model):
		D=model;C=purchase_date;B=interaction;A=self
		try:
			F=datetime.strptime(C,'%Y-%m-%d')
			if F>datetime.now():await B.response.send_message('Purchase date cannot be in the future.',ephemeral=_D);return
		except ValueError:await B.response.send_message('Invalid date format. Please use YYYY-MM-DD.',ephemeral=_D);return
		E=A.load_json_file(A.user_info_file);E[str(B.user.id)]={_F:C,'model':D};A.save_json_file(E,A.user_info_file);await B.response.send_message(f"AirPods information updated. Model: {D}, Purchase Date: {C}",ephemeral=_D)
	@app_commands.command(name='battery_health',description='View comprehensive AirPods battery health and statistics')
	@app_commands.describe(user='The user to check the battery health for (leave empty for yourself)')
	async def battery_health(self,interaction,user=None):
		a='Date';Z='Case';Y='Right AirPod';X='Left AirPod';J=interaction;I=False;C=self;K=J.user if user is None else user;F=str(K.id);L=C.load_json_file(C.battery_log_file);M=C.load_json_file(C.user_info_file)
		if F not in L or not L[F]:await J.response.send_message(f"No battery data logged yet for {K.mention}. Use /log_battery to start tracking.",ephemeral=_D);return
		if F not in M:await J.response.send_message(f"AirPods information not set for {K.mention}. Use /set_airpods_info to set it.",ephemeral=_D);return
		await J.response.defer();A=L[F];N=M[F][_F];Q=M[F]['model'];G=C.estimate_max_capacity(A,N);b=sum(A[_A]for A in A);c=sum(A[_B]for A in A);d=sum(A[_C]for A in A);e=b/len(A);f=c/len(A);g=d/len(A)
		if len(A)>1:h=C.parse_timestamp(A[0][_E]);i=C.parse_timestamp(A[-1][_E]);O=(i-h).days or 1;R=(A[0][_A]-A[-1][_A])/O;S=(A[0][_B]-A[-1][_B])/O;T=(A[0][_C]-A[-1][_C])/O
		else:R=S=T=0
		o,(D,E)=plt.subplots(2,1,figsize=(10,12));H=[C.parse_timestamp(A[_E])for A in A];U=[A[_A]for A in A];V=[A[_B]for A in A];W=[A[_C]for A in A];D.plot(H,U,label=X);D.plot(H,V,label=Y);D.plot(H,W,label=Z);D.set_title(f"AirPods Battery Levels Over Time ({Q})");D.set_xlabel(a);D.set_ylabel('Battery Percentage');D.legend();D.tick_params(axis='x',rotation=45);j=[A/G[_A]*100 for A in U];k=[A/G[_B]*100 for A in V];l=[A/G[_C]*100 for A in W];E.plot(H,j,label=X);E.plot(H,k,label=Y);E.plot(H,l,label=Z);E.set_title('Estimated Battery Health Trend');E.set_xlabel(a);E.set_ylabel('Estimated Health Percentage');E.legend();E.tick_params(axis='x',rotation=45);plt.tight_layout();P=io.BytesIO();plt.savefig(P,format='png');P.seek(0);m=discord.File(P,filename='battery_health_stats.png');n=(datetime.now()-datetime.fromisoformat(N)).days;B=discord.Embed(title=f"AirPods Battery Health and Stats for {K.mention}",color=discord.Color.blue());B.add_field(name='AirPods Info',value=f"Model: {Q}\nPurchase Date: {N}\nDays Owned: {n}",inline=I);B.add_field(name='Estimated Maximum Capacity',value=f"Left: {G[_A]:.2f}%\nRight: {G[_B]:.2f}%\nCase: {G[_C]:.2f}%",inline=I);B.add_field(name='Average Battery Levels',value=f"Left: {e:.2f}%\nRight: {f:.2f}%\nCase: {g:.2f}%",inline=I);B.add_field(name='Daily Battery Drain Rate',value=f"Left: {R:.2f}%\nRight: {S:.2f}%\nCase: {T:.2f}%",inline=I);B.add_field(name='Latest Battery Levels',value=f"Left: {A[-1][_A]}%\nRight: {A[-1][_B]}%\nCase: {A[-1][_C]}%",inline=I);B.add_field(name='Total Logs',value=f"{len(A)} entries",inline=I);B.set_image(url='attachment://battery_health_stats.png');B.set_footer(text='Battery health is an estimation based on logged data and purchase date. It may not be 100% accurate.');await J.followup.send(embed=B,file=m,ephemeral=_D)
	@app_commands.command(name='clear_battery_logs',description='Clear your AirPods battery logs')
	async def clear_battery_logs(self,interaction):
		B=interaction;C=str(B.user.id);A=self.load_battery_log()
		if C not in A or not A[C]:await B.response.send_message('No battery data found to clear.',ephemeral=_D);return
		del A[C];self.save_battery_log(A);await B.response.send_message('Your battery logs have been cleared.',ephemeral=_D)
async def setup(bot):await bot.add_cog(AirPodsBatteryTrackerCog(bot))