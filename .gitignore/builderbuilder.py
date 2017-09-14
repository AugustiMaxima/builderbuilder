#requirement: closing brackets should not be on the same line as a variable declaration.
#dont include the methods in your source

def builderbuilder(location,destination):
        source=open(location,"r");
        ns=source.readline()[:-1].split(':')[0].split('{')[0].split(' ');
        while(ns[-1]==''):
                ns.pop();
        classname=ns[-1];
        fields=[];
        for line in source.readlines():
                if(';' in line):
                        #c,c++,c# and java deals with naming based on whitespace
                        words=line.split(';')[0].split('=')[0].split(' ');
                        #the if statement below are to deal with the general format of variable declarations i.e public string k='ss';
                        #the preprocessing intends to strip out the relevant bits, the type string and the variable name k
                        #whether its k="ss"; k="ss" or just k, this will extract the k;
                        fields.append((words[-2:]));#the last two element of the splice : type, name
        source.close();
        out = open(destination,"w");
        out.write("public class "+classname+"Builder\n");
        out.write("{\n");
        for pair in fields:
                out.write("\tprivate "+pair[0]+" "+pair[1]+";\n");
        out.write("\n");
        for pair in fields:
                out.write("\tpublic "+classname+"Builder "+"Set"+pair[1][0].capitalize()+pair[1][1:]+"("+pair[0]+" "+pair[1]+"){\n");
                out.write("\t\tthis."+pair[1]+"="+pair[1]+";\n");
                out.write("\t\treturn this;\n");
                out.write("\t}\n\n");
        out.write("\tpublic "+classname+" Build(){\n")
        initializer="{\n"
        i=len(fields);
        for pair in fields:
                i=i-1;
                initializer+="\t\t"+pair[1]+"="+pair[1];
                if i:
                        initializer+=",\n";
        initializer+="\n\t\t};\n";
        out.write("\t\t"+"return new "+classname+initializer);
        out.write("\t}\n");
        out.write("}\n");
        out.close();