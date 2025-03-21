import matplotlib.pyplot as pt


def focus_graph():
    file = open("TimeNote/focus.txt","r")
    content = file.read()
    file.close()
    
    content = content.split(",")
    #coordinates for graphing
    x1 = []
    for i in range(0,len(content)):
        content[i] = float(content[i]) #changing to float because stored in string in teh txt file
        x1.append(i)

    print(content)
    ''' IF u want to restart the graph freshly go to focus.txt clear all data except 0'''
    
    y1 = content
    
    # ploat the graph  
    #plot on x axes = 0.01 is 1 mintes 
    #on y axes 1 = one time into focus mode
    pt.plot(x1,y1,color = "blue",marker  = "o")
    pt.title("Your Focused Time",fontsize = 16)
    pt.xlabel("Times your Entered Focus Mode", fontsize = 14)
    pt.ylabel("Focus Time",fontsize=14)
    pt.grid()
    pt.show()
