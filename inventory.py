import mysql.connector
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="12345678",
    database="inventory1"
    )
mycursor=mydb.cursor()
c=1;

print("chooseuser=\n1:temprory\n2:management")
a=int(input("management needs passwd\nenter choice"))
if(a==1):
    c=int(input("1:import,2:export"))
    if(c==1):
        while(1):
            print("1:adding\n2:todays import\n3:todays order entery\n4:todays desc order entry\n5:go back ")
            b=int(input("input choice:"))
            if(b==1):
                form="insert into import(srno,description,quantity,rate,seller,date,time) values (%s,%s,%s,%s,%s,now(),now())"
                import1=(int(input("srno")),input("description"),int(input("quantity")),int(input("rate")),input("seller"))
                mycursor.execute(form,import1)
                mydb.commit()

                mycursor.execute("update  import set amount=rate*quantity")
                mydb.commit()
            if(b==2):
                mycursor.execute("select %s from import where date=curdate()"%(input("attribute")))
                m=mycursor.fetchall()
                for r in m:
                    print(r)
            if(b==3):
                mycursor.execute("select %s from import where date =curdate() order by %s"%(input("attribute"),input("order by attribute")))
                anil = mycursor.fetchall()
                for r in anil:
                    print(r)
            if(b==4):
                mycursor.execute("select %s from import where date =curdate() order by %s desc" % (input("attribute"), input("order by attribute")))
                anil = mycursor.fetchall()
                for r in anil:
                    print(r)
            if(b==5):
                break
    if(c==2):
        while (1):
            print("1:adding\n2:todays import\n3:todays order entery\n4:todays desc order entry\n5:go back")
            b = int(input("choice"))
            if (b == 1):
                form = "insert into export(srno,id,description,quantity,rate,buyer,date,time) values (%s,%s,%s,%s,%s,%s,now(),now())"
                import1 = (
                int(input("srno")),int(input("id")), input("description"), int(input("quantity")), int(input("rate")), input("buyer"))
                mycursor.execute(form, import1)
                mydb.commit()

                mycursor.execute("update  export set amount=rate*quantity")
                mydb.commit()
            if (b == 2):
                mycursor.execute("select %s from export where date=curdate()" % (input("attribute")))
                m = mycursor.fetchall()
                for r in m:
                    print(r)
            if (b == 3):
                mycursor.execute("select %s from export where date =curdate() order by %s" % (
                input("attribute"), input("order by attribute")))
                anil = mycursor.fetchall()
                for r in anil:
                    print(r)
            if (b == 4):
                mycursor.execute("select %s from export where date =curdate() order by %s desc" % (
                input("attribute"), input("order by attribute")))
                anil = mycursor.fetchall()
                for r in anil:
                    print(r)
            if(b==5):
                break



if(a==2):
    while(c<=3):
        c=c+1;
        z=12345678;
        b=int(input("Enter your passwd:"))
        if(b==z):
            while (1):
                print("access granted")
                print("1:import\n2:export\n3:profit and loss\n4:sequrity updates\n5:go back")
                e=int(input("enter choice:"))
                if(e==1):
                    print("getting in import:")
                    g=int(input("choose option"))
                    if(g==1):
                        form = "insert into import(srno,description,quantity,rate,seller,date,time) values (%s,%s,%s,%s,%s,now(),now())"
                        import1 = (int(input("srno")), input("description"), int(input("quantity")), int(input("rate")),
                                   input("seller"))
                        mycursor.execute(form, import1)
                        mydb.commit()

                        mycursor.execute("update  import set amount=rate*quantity")
                        mydb.commit()
                    if(g==2):
                        mycursor.execute("select %s from import where date=%s" % (input("attribute")),input("date"))
                        m = mycursor.fetchall()
                        for r in m:
                            print(r)
                    if(g==3):
                        mycursor.execute("select *from import")
                        m=mycursor.fetchall()
                        for r in m:
                            print(r)
                    if(g==4):
                        mycursor.execute("select %s from import where order by %s" % (
                            input("attribute"), input("order by attribute")))
                        anil = mycursor.fetchall()
                        for r in anil:
                            print(r)
                    if(g==5):
                        mycursor.execute("select %s from export where  order by %s desc" % (
                            input("attribute"), input("order by attribute")))
                        anil = mycursor.fetchall()
                        for r in anil:
                            print(r)
                    if(g==6):

                        mycursor.execute("delete * from import where srno=%"%(int(input("srno"))))
                        mydb.commit()
                    if(g==7):
                        mycursor.execute("update import set % =%s where srno=%s"%(input("attribute"),int(input("value")),int(input("srno"))))
                        mydb.commit()
                    if(g==8):
                        break


                if(e==2):
                    print("getting in export")
                    g=int(input("choose option"))
                    if(g==1):
                        form = "insert into export(srno,id,description,quantity,rate,buyer,date,time) values (%s,%S,%s,%s,%s,%s,now(),now())"
                        import1 = (int(input("srno")),int(input("id")), input("description"), int(input("quantity")), int(input("rate")),
                                   input("buyer"))
                        mycursor.execute(form, import1)
                        mydb.commit()

                        mycursor.execute("update  export set amount=rate*quantity")
                        mydb.commit()
                    if(g==2):
                        mycursor.execute("select %s from export where date=%s" % (input("attribute")), input("date"))
                        m = mycursor.fetchall()
                        for r in m:
                            print(r)
                    if(g==3):
                        mycursor.execute("select *from export")
                        m = mycursor.fetchall()
                        for r in m:
                            print(r)
                    if(g==4):
                        mycursor.execute("select %s from export where order by %s" % (
                            input("attribute"), input("order by attribute")))
                        anil = mycursor.fetchall()
                        for r in anil:
                            print(r)
                    if(g==5):
                        mycursor.execute("select %s from export where order by %s desc" % (
                            input("attribute"), input("order by attribute")))
                        anil = mycursor.fetchall()
                        for r in anil:
                            print(r)
                    if(g==6):

                        mycursor.execute("delete * from export where srno=%"%(int(input("srno"))))
                        mydb.commit()
                    if(g==7):
                        mycursor.execute("update export set % =%s where srno=%s"%(input("attribute"),int(input("value")),int(input("srno"))))
                        mydb.commit()
                    if(g==8):
                        break
                if(e==3):
                    print("getting in profit and loss")
                    mycursor.execute("select amount from import from date between(%s to %s)"%(input("from:"),inpyt("to:")))
                    mylamp=mycursor.fetchall()
                    q=1;
                    for r in mtlamp:
                        q=q+r;
                    mycursor.execute(
                        "select amount from export from date between(%s to %s)" % (input("from:"), input("to:")))
                    mylamp = mycursor.fetchall()
                    s = 1;
                    for r in mtlamp:
                        s = s + r;
                    t=s-q;
                    if(t>=0):
                        print("profit:"+t)
                    else:
                        print("loss"+t)
                if(e==4):
                    print("enter new passwd")
                    z=int(input("passwd"))
                    break
                if(e==5):
                    break
        else:
            print("incorrect  password \ntry again")
