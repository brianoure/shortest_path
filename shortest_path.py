"""
Find the shortest path between the start_node and the end_node as described by the network_description_list
"""

"""[[start,end,reverse,distance]...]"""
nodes = 5
network = [
            [0,1,1,150],
            [0,2,1,250],
            [0,3,1,450],
            [1,2,1,750],
            [1,4,1,650],
            [2,3,1,250],
            [3,4,1,550],
            [4,2,1,350]            
          ]
startNode_endNode_query_list = [1,3]
mybase        = nodes

class BRANCH:
    def __init__(this,start,end,distance):
        this.start   = start
        this.end     = end
        this.distance= distance

class ROUTE:
    def __init__(this,node_list,route_distance):
        this.node_list      = node_list
        this.route_distance = route_distance

def base_list_to_number(mylist,mybase):
    #MSB on the left of list,LSB on the right of list
    mylist_length = len(mylist)
    rslt = 0
    for t in range((mylist_length-1),-1,-1):
        rslt = rslt + (mylist[t]*(mybase**t))
    return rslt
       
def reverse_list(mylist):
    #Pride: I really prefer to make my own functions
    rslt = []
    copy_list = mylist[0:]
    for j in range( (len(mylist)-1),-1,-1 ):
        rslt = rslt + [copy_list[j]]
    return rslt

def number_to_base_list(mynumber,mybase):
    #Convert a decimal(base 10) number to a specified base(mybase) and store the resultant digits in a list.(MSB is index zero)
    base_power    = 0
    loop_continue = 1
    rslt = []
    while(loop_continue):
        myfloor = (mynumber//(mybase**base_power))//mybase
        myrem   = (mynumber//(mybase**base_power))% mybase
        rslt    = rslt + [myrem]
        base_power = base_power + 1
        if(myfloor==0):
            loop_continue=0
    rslt_length = len(rslt)
    return ([0]*(nodes-rslt_length))+reverse_list(rslt)

def all_list_item_equal(mylist):
    #Just checking to see if all items are equal
    rslt = True
    listlength = len(mylist)
    if(listlength==1):
        return rslt
    first = mylist[0]
    for x in range(1,listlength):
        rslt = rslt and(first==mylist[x])
    return rslt

def node_distance(a,b,mybranches_list):
    #Get the distance between the nodes specified by the indices a and b
    branches_list_length = len(mybranches_list)
    if(a==b):
        return 0
    for j in range( branches_list_length ):
        if(mybranches_list[j].start==a)and(mybranches_list[j].end==b):
            return mybranches_list[j].distance
    return "branch doesn't exist"

def distance_covered(num_list,mybranches_list):
    #Get the distance covered if we have a node sequence(sequence_list)
    if(all_list_item_equal(num_list)):
        return 0
    num_list_length    = len(num_list)
    distances_list     = []
    continue_function  = True
    x=0
    while( x<num_list_length ):
        if( not(x==num_list_length-1) ):
            nodal_distance = node_distance(num_list[x],num_list[x+1],mybranches_list)
            if( nodal_distance=="branch doesn't exist" ):
                continue_function=False
                break
            else:
                distances_list = distances_list + [ nodal_distance ]
        x = x+1
    if(continue_function==False):
        return "branch doesn't exist"
    total_dist=0
    for x in range(len(distances_list)):
        total_dist = total_dist + distances_list[x]
    return total_dist

def list_startWith_endwith(start,end,sequence_list):
    sequence_list_length = len(sequence_list)
    return ( (sequence_list[0]==start) and (sequence_list[sequence_list_length-1]==end) ) 
    

def list_has_startValue_and_endsWith(start,end,mylist):
    starting = False
    mylist_length = len(mylist)
    for j in range(1,(mylist_length-2)):
        if(mylist[j]==start):
            starting=True
    return (starting and (mylist[mylist_length-1]==end))


def shortest_path(network__description_list,start_end_nodes_query_list):
    #Create all the possibilities given the path reversible flags i.e branches_list[2]
    mybranches_list=[]
    for x in range(len(network)):
        if(network[x][2]):
            mybranches_list = mybranches_list + [ BRANCH( network[x][0],network[x][1],network[x][3]) ]
            mybranches_list = mybranches_list + [ BRANCH( network[x][1],network[x][0],network[x][3]) ]
        if(not(network[x][2])):
            mybranches_list = mybranches_list + [ BRANCH( network[x][0],network[x][1],network[x][3]) ]
    route_list     = []
    for possibility in range(nodes**nodes):
        num_list   = number_to_base_list(possibility,mybase)
        mydistance = distance_covered(num_list,mybranches_list)
        route_list = route_list + [ROUTE( num_list,mydistance )]
    #for y in range(len(route_list)):print(route_list[y].node_list,route_list[y].route_distance)

    """MOD"""    
    selected_route_list = []
    for h in range(len(route_list)):
        the_list_length = len(route_list[h].node_list)
        if( (route_list[h].node_list[0]==startNode_endNode_query_list[0]) and (route_list[h].node_list[the_list_length-1]==startNode_endNode_query_list[1]) ):
            if(not(type(route_list[h].route_distance)==type(""))):
                selected_route_list = selected_route_list + [ route_list[h] ]
    for y in range(len(selected_route_list)):print(selected_route_list[y].node_list,selected_route_list[y].route_distance)
    """MOD"""

    route_list_least_index = 0
    y = 0
    the_maximum = len(selected_route_list)
    while (y<the_maximum):
        if( selected_route_list[y].route_distance<selected_route_list[route_list_least_index].route_distance ):
            route_list_least_index = y
        y = y+1
    return [ selected_route_list[route_list_least_index].node_list , selected_route_list[route_list_least_index].route_distance ]

print(shortest_path(network,startNode_endNode_query_list))

