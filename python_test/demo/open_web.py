a = """
时间网站
https://so.csdn.net
https://stackoverflow.com/
https://doc.weixin.qq.com/
https://ocw.mit.edu
https://laravelacademy.org/
https://www.usenix.org/
https://developer.apple.com
https://blog.csdn.net
https://docs.qq.com
https://github.com
https://www.jmlr.org
https://arxiv.org/
https://www.jianshu.com
https://showmeai.tech
https://sms-activate.org/getNumber
https://www.emnlp2015.org
https://mooc.study.163.com
https://blog.51cto.com
https://meeting.tencent.com
https://spongecaptain.cool
https://www.usenix.org
https://zhuanlan.zhihu.com
https://www.cnblogs.com
https://docs.python.org
https://www.cnblogs.com
http://192.168.0.1
https://www.w3schools.com
https://www.ipaddress.com

https://www.slimjet.com
https://mail.163.com
https://onedrive.live.com
https://mirrors.tencent.com
https://www.cs.usfca.edu
https://www.sojson.com
https://docs.oracle.com/
https://screen.bmcx.com
https://pkg.go.dev
https://console.cloud.tencent.com
https://prometheus.io
https://geektutu.com
https://developers.google.com
https://tryhackme.com
https://grafana.com
https://buy.cloud.tencent.com
https://ke.qq.com/
https://vimeo.com
http://www.coder100.com
https://mvnrepository.com/
https://www.ac-paris.fr
https://community.jalios.com
https://www.usenix.org
https://msjw.ga.sz.gov.cn

https://www.gezila.com
https://www.biaodianfu.com
https://zhuanlan.zhihu.com
https://www.fujieace.com
https://www.computerworld.com
https://docs.docker.com
www.ruanyifeng.com
https://www.amazon.com
https://www.rfi.fr
https://amr.sz.gov.cn
https://sipub.sz.gov.cn
http://www.eesc.com.cn
https://bitly.com/!!!
https://visualgo.net
http://tool.manmanbuy.com
https://www.luomapan.com
http://www.stegd.edu.cn
https://www.eeagd.edu.cn
http://www.zikaogd.com
http://gzzk.gz.gov.cn
https://laravelacademy.org
https://www.usenix.org
http://www.4k8k.xyz

https://mp.weixin.qq.com

https://www.aliyundrive.com
#
https://i.csdn.net/
https://deepspeech.readthedocs.io/
https://wenku.csdn.net/
http://cn.voidcc.com/

https://dotnet.microsoft.com/
https://codeleading.com/article/23783836829/

https://mail.google.com



https://passport.xfyun.cn/
"""

lst = a.split('\n')
lst_new = [str("%s").replace("'", '"') % item for item in lst if item]
print(str(lst_new).replace("'", '"'))
# for item in lst_new:
#     print('"%s",' % item)
