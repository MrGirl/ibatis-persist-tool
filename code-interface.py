#filenames=["Alarm_rule","Application","Collector_app","Collector_base","Collector_system","Data_model","Device_base","Domain_monitor","Domain_superagent","Domain","Machine_room","Monitor_item_config_argument","Monitor_item_config","Monitor_item_host","Monitor_item_status_host","Node","Sentry_group","Sentry_server","Server_disk","Server_memory","Server_network_card","Server_os","Server_pci"]
from datetime import date
import sys
if __name__ == "__main__":
    if len(sys.argv) <=1:
        print 'please enter Interface prefix,eg:python code-interace AlarmRule'
        sys.exit(-1)
    filenames=[]
    filenames=sys.argv[1:]
    for filename in filenames:
        f_w_name = "I"+filename+"Service.java"
        f_w = open(f_w_name,"w")
        f_w.write("package com.netease.sentry.biz.service;\n")
        f_w.write("import java.util.List;\n")
        f_w.write("import java.util.Map;\n")
    
        f_w.write("import com.netease.sentry.biz.domain."+filename+";\n")
        f_w.write("/**\n");
        f_w.write(" * @author hzzhangyuandao\n");
        f_w.write(" * @since "+str(date.today()));
        f_w.write(" */\n");
    
        f_w.write("public interface "+"I"+filename+"Service {\n");
    
        f_w.write("public int create("+filename+" "+filename.lower()+");\n");
        f_w.write("public int remove(int id);\n");
        f_w.write("public int update("+filename+" "+filename.lower()+");\n");
        f_w.write("public "+filename+" retrieve(Map<Object,Object> params);\n");
        f_w.write("public List<"+filename+"> list(Map<Object,Object> params);\n");
        f_w.write("}");
        f_w.close();