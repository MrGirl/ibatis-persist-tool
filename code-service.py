from datetime import date
import sys
if __name__ == '__main__':
    if len(sys.argv)<=1:
        print 'please enter the Service prefix name , separated by space.'
        sys.exit(0)
    print "yes !"
    filenames = sys.argv[1:]
    for filename in filenames:
        f_w_name = filename+"Service.java"
        f_w = open(f_w_name,"w")

        importstr = '''
        package com.netease.sentry.biz.service.impl;

        import java.util.List;
        import java.util.Map;

        import javax.annotation.Resource;

        import org.springframework.stereotype.Component;

        import com.netease.sentry.biz.dao.SqlDao;'''
        importstr=importstr+"import com.netease.sentry.biz.domain."+filename+";\n";
        importstr=importstr+"import com.netease.sentry.biz.service."+"I"+filename+"Service;\n"

        
        v='''
        /**
         * @author hzzhangyuandao
         * @since '''
        v+=str(date.today())
        v+='''
         */
        @Component
        '''

        importstr=importstr+v

        f_w.write(importstr+"\n");

        f_w.write("public class "+filename+"Service"+" implements "+"I"+filename+"Service {\n");
        f_w.write("@Resource(name=\"sqlDao\")\n");
        f_w.write("private SqlDao sqlDao;\n");

        f_w.write("@Override\n");
        f_w.write("public int create("+filename+" "+filename.lower()+"){\n");
        f_w.write("return sqlDao.create(\""+filename+".create"+"\","+filename.lower()+");\n");
        f_w.write("}\n");


        #remove
        f_w.write("@Override\n");
        f_w.write("public int remove(int id) {\n");
        f_w.write("return sqlDao.delete(\"");
        f_w.write(filename+".delete\",id);\n");
        f_w.write("}\n");


        #update
        f_w.write("@Override\n");
        f_w.write("public int update("+filename+" "+filename.lower()+"){\n");
        f_w.write("return sqlDao.update(\""+filename+".update"+"\","+filename.lower()+");\n");
        f_w.write("}\n");

        #retrieve
        f_w.write("@Override\n");
        f_w.write("public "+filename+" retrieve(Map<Object, Object> params) {\n");
        f_w.write("return "+"("+filename+")"+"sqlDao.retrieve(\""+filename+".retrieve\",params);\n");
        f_w.write("}\n");


        #retrieve
        f_w.write("@Override\n");
        f_w.write("@SuppressWarnings(\"unchecked\")");
        f_w.write("public List<"+filename+"> list(Map<Object, Object> params) {\n");
        f_w.write("return "+"(List<"+filename+">)"+"sqlDao.list(\""+filename+".retrieve\",params);\n");
        f_w.write("}\n");

        f_w.write("}");

        print(sys.argv[0]);
        print(sys.argv[1]);