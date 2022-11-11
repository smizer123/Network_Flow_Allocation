import math

class Edge:
    def __init__(self,edge):
        """
        Create a edge object, storing the edges inside the adj_list network flow graph, and also it reverse edges
        :Input: edges in form of [node,flow]
        :Output, return or postcondition: A edge
        :Time complexity: O(1), initialise the edge cost constant in time
        :Aux space complexity: O(1) initialise the edge cost constant in space
        """
        self.edge = edge
        self.reverse = None

    def add_reverse(self,edge):
        """
        assign the reversed edge of this edges
        :Input: edges in form of [node,flow]
        :Output, return or postcondition: assign the reversed edge of this edges
        :Time complexity: O(1), assigning the edge cost constant in time
        :Aux space complexity: O(1) assigning the edge cost constant in space
        """
        self.reverse = edge

    def see_edge(self):
        """
        return the edge
        :Input:
        :Output, return or postcondition: return the edge
        :Time complexity: O(1), return the edge cost constant in time
        :Aux space complexity: O(1) return the edge cost constant in space
        """
        return self.edge

    def reverse(self):
        """
        return the reversed edge
        :Input:
        :Output, return or postcondition: return the reversed edge
        :Time complexity: O(1), return the reversed edge cost constant in time
        :Aux space complexity: O(1) return the reversed edge cost constant in space
        """
        return self.reverse
def adj_list(a):
    """
    Create a adjacency list Residual network flow graph for the given time table(availability), the graph will create
    1 default nodes for each person, 3 source nodes with 1 super source connect to 2 other sources, then 2 sinks with 1
    super sink, each day will be split into 4 node, a morning, night, morning night and day nodes:
    #s,s1,s2,0,1,2,3,4,5,e,e2, m, n,mn,days
    #0, 1, 2,3,4,5,6,7,8,9,10,11,12,13,14
    the above will the be location, and also a variable name for each nodes
    s will connect to -> s1, s2, a path to s1 will have the capacity of the total of minimum_meal*5(each person)
                                 a path to s2 will have  the capacity of total_meal - (minimum_meal*5)

    s1, will connect to -> 0,1,2,3,4
                            each edges from s1 to 0,1,2,3,4 will have the capacity = the minimum amount of meal day
                            allow for the entire time table
    s2 will connect to -> 0,1,2,3,4,5
                            each edges from s2 to 0,1,2,3,4,5 will have the capacity = the maximum_meal - minimum_meal
                            and 5 will be the restaurant
    each 0,1,2,3,4,5 will connect to m,n,mn,days node accordingly by there availability
                     each edges to morning, night, morning or night vertex will have a capacity of 1
                     except for the edges coming our of 5 will always have the capacity of 5 and also always connect
                     to mn.
    mn -> m,n : a morning night vertex indicate that that person a able to do either, the capacity for each edges
                will be 1

    m,n -> day : each edges from morning and day will have a capacity of 1 and going to day, and the total flow
                received = 2 which is from m,n

    day -> e : e will be the first sink, which will received 2 capacity of flow from each day, and the total flow
                received = day * n

    e -> e2 : which is the sink to the super sink, which e2 will received a capacity = total amount of meal
    :Input: a list of lists availability for each person each day
            For a person numbered j and day numbered i, availability[i][j] is equal to:
            0, if that person has neither time availability to prepare the breakfast nor the dinner
            during that day.
            if that person only has time availability to prepare the breakfast during that day.
            if that person only has time availability to prepare the dinner during that day.
            if that person has time availability to prepare either the breakfast or the dinner during
            that day.

    argv1: a : a list of lists availability
    :Output, return or postcondition: a adjacency list Residual network flow graph for the given time table(availability)
    :Time complexity: creating a adj_list, which the amount of vertex will V = n * 4 because each day will need 4 nodes
                        of m,n,mn,day and the amount of edges will be E = n * 9 which include 5 according by the
                        availability, 4 difference to connect m,n,mn,day
                        -> the time complexity O(V+E) but we know that V = n * 4, E = n * 9 so the overall time
                        complexity will be O(n)
                        where n is the number of days
    :Aux space complexity:creating a adj_list, which the amount of vertex will V = n * 4 because each day will need 4 nodes
                        of m,n,mn,day and the amount of edges will be E = n * 9 which include 5 according by the
                        availability, 4 difference to connect m,n,mn,day
                        -> the space complexity O(V+E) but we know that V = n * 4, E = n * 9 so the overall space
                        complexity will be O(n)
                        where n is the number of days
    """

    adj_lst = [[] for i in range((len(a)*4)+11)]
    #s,s1,s2,0,1,2,3,4,5,e,e2, m, n,mn,days
    #0, 1, 2,3,4,5,6,7,8,9,10,11,12,13,14

    no_day = len(a)
    minimum_meal = math.floor(no_day*0.36)
    maximum_meal = math.ceil(no_day*0.44)
    restaurant_meal = math.floor(no_day*0.1)
    total_no_meal = no_day*2
    day_position = 14 # the position of day
    mn_position = 13 # morning_night position in the graph
    m_position = 11 # morning position
    n_position = 12# night position
    sink_postion = 9 # first sink position
    ul_sink_position = 10 # ultimate sink position
    restaurant_position = 8
    p = None
    q = None
    # initialise source(s)
    # s-> s1,s2
    # s will connect to s1 & s2
    # from s to s1, we will have the capacity of minimum_meal*5
    # from s to s2, we will have  the capacity of total_meal - (minimum_meal*5)
    # all together will add up to  the total amount of meal = (number of day) * 2

    p = Edge([1,0])
    q = Edge([0,minimum_meal*5])
    q.add_reverse(p)
    p.add_reverse(q)
    adj_lst[0].append(p)
    adj_lst[1].append(q)

    p = Edge([2, 0])
    q = Edge([0, total_no_meal-(minimum_meal*5)])
    q.add_reverse(p)
    p.add_reverse(q)
    adj_lst[0].append(p)
    adj_lst[2].append(q)

    # adj_lst[0].append([1,minimum_meal*5])
    # adj_lst[0].append([2,total_no_meal-(minimum_meal*5)])

    # s1 -> 0,1,2,3,4
    # initialise value of s1
    # where s1 will have 5 edge connect toward all the vertex represent the 5 people in the house
    # and every edge will have the capacity = the minimum amount of meal that each person need to have
    for i in range(3,8,1):
        # adj_lst[1].append([i,minimum_meal])
        p = Edge([i, 0])
        q = Edge([1, minimum_meal])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[1].append(p)
        adj_lst[i].append(q)
    # s2 -> 0,1,2,3,4,5
    # initialise value of s2
    # where s2 will have 6 edge connect toward all the vertex represent the 5 people in the house and the restaurant
    # each edge connect with a persin will have the capacity = the maximum_meal - minimum_meal
    # and restaurant will have the capacity of : restaurant_meal

    for i in range(3,8,1):
        # adj_lst[2].append([i,maximum_meal-minimum_meal])
        p = Edge([i, 0])
        q = Edge([2, maximum_meal-minimum_meal])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[2].append(p)
        adj_lst[i].append(q)

    # adj_lst[2].append([8,restaurant_meal])
    p = Edge([8, 0])
    q = Edge([2, restaurant_meal])
    q.add_reverse(p)
    p.add_reverse(q)
    adj_lst[2].append(p)
    adj_lst[8].append(q)

    #mn -> n and m
    # initialise morning, night, and morning or night vertex
    # morning or night vertex will 2 paths to connect toward night and morning vertex, each will have a capacity of 1

    for i in range(len(a)):
        # adj_lst[mn_position+i*4].append([m_position+i*4,1]) # because the position of the next day mn_position will =
                                                            # mn_position + 4
        p = Edge([m_position+i*4, 0])
        q = Edge([mn_position+i*4, 1])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[mn_position+i*4].append(p)
        adj_lst[m_position+i*4].append(q)

        # adj_lst[mn_position+i*4].append([n_position+i*4,1])

        p = Edge([n_position + i * 4, 0])
        q = Edge([mn_position + i * 4, 1])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[mn_position + i * 4].append(p)
        adj_lst[n_position + i * 4].append(q)

    #m and n -> day
    # now connect all the morning and night vertex to the day vertex
    # where an edge will from monring to day, night to day and will have the capacity of 1
    # which will indicate each day only able to have 2 meal
    for i in range(len(a)):
        # adj_lst[m_position + i * 4].append([day_position+i*4, 1])

        p = Edge([day_position+i*4, 0])
        q = Edge([m_position + i * 4, 1])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[m_position + i * 4].append(p)
        adj_lst[day_position+i*4].append(q)

        # adj_lst[n_position + i * 4].append([day_position+i*4, 1])

        p = Edge([day_position + i * 4, 0])
        q = Edge([n_position + i * 4, 1])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[n_position + i * 4].append(p)
        adj_lst[day_position + i * 4].append(q)
    # day -> sink
    # each day will have in comming flow 2
    # create a sink which will received all the out coming flow of each day

    for i in range(len(a)):
        # adj_lst[day_position +i*4].append([sink_postion,2])

        p = Edge([sink_postion, 0])
        q = Edge([day_position +i*4, 2])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[day_position+i*4].append(p)
        adj_lst[sink_postion].append(q)

    # sink -> ultimate sink
    # then I will create an ultimate sink, which received exactly the capacity of total_meal

    # adj_lst[sink_postion].append([ul_sink_position,total_no_meal])

    p = Edge([ul_sink_position, 0])
    q = Edge([sink_postion, total_no_meal])
    q.add_reverse(p)
    p.add_reverse(q)
    adj_lst[sink_postion].append(p)
    adj_lst[ul_sink_position].append(q)

    # each person vertex and restaurant will connect to either morning, night, morning or night vertex if there
    # availability allow or won't if they are not free on that day
    # each edges to morning, night, morning or night vertex will have a capacity of 1

    #housemates -> m,n,mn of all days
    for day in range(len(a)):
        for person in range(len(a[day])):
            if a[day][person] == 1:
                # adj_lst[person+3].append([m_position+day*4,1])

                p = Edge([m_position+day*4, 0])
                q = Edge([person+3, 1])
                q.add_reverse(p)
                p.add_reverse(q)
                adj_lst[person+3].append(p)
                adj_lst[m_position+day*4].append(q)

            elif a[day][person] == 2:
                # adj_lst[person+3].append([n_position+day*4,1])

                p = Edge([n_position + day * 4, 0])
                q = Edge([person + 3, 1])
                q.add_reverse(p)
                p.add_reverse(q)
                adj_lst[person + 3].append(p)
                adj_lst[n_position + day * 4].append(q)

            elif a[day][person] == 3:
                # adj_lst[person+3].append([mn_position+day*4,1])

                p = Edge([mn_position + day * 4, 0])
                q = Edge([person + 3, 1])
                q.add_reverse(p)
                p.add_reverse(q)
                adj_lst[person + 3].append(p)
                adj_lst[mn_position + day * 4].append(q)

    #restaurant -> mn of all days

    for i in range(len(a)):
        # adj_lst[restaurant_position].append([mn_position+i*4,1])
        p = Edge([mn_position+i*4, 0])
        q = Edge([restaurant_position, 2])
        q.add_reverse(p)
        p.add_reverse(q)
        adj_lst[restaurant_position].append(p)
        adj_lst[mn_position+i*4].append(q)

    # print(no_day,minimum_meal,maximum_meal,restaurant_meal)
    return adj_lst
def ford_fulkerson(availability):
    """
    Implementation of Ford Fulkerson algorithm, with the help of dfs, running through a given network flow adjacency
    list graph to find the maximum flow,by finding all the available path with until there no more path the it could
    take, return the maximum flow that that path can took and add to the flow, repeated until no more path can take.
    returning a maximum flow that can go through the entire graph, and modified the input graph with the path to
    get that maximum flow
    :Input: a adjacency list Residual network flow graph for the given time table(availability)
    argv1: availability : a adjacency list Residual network flow graph for the given time table(availability)
    :Output, return or postcondition: a maximum flow that can go through that graph, and modified the existed graph
                                        with suitable path to get the maximum flow
    :Time complexity: Doing dfs for F time in the worst case where F is the maximum flow of the graph, we know that
                      doing dfs will cost O(V+E) time, doing it F time will give you a complexity of O(EF)
                      where E is the number of edges in the graph, but we know that the maximum flow of the graph
                      = n*2 (number of meals) where n is number of days. And by the characteristic of our graph, we know
                      that the time it took to a dfs one time on the graph is O(n) where n is the number of day.
                      -> so the overall time complexity will O(n^2)
    :Aux space complexity: initialise of visited will cause O(n) where n is the number of day
                            -> also we are getting the input of a adjacency list Residual network
                            flow graph for the given time table(availability) which have over space complexity of O(n)
                            ->therefore the overall space complexity will be O(n)
    """
    flow = 0
    augment = 0.2
    while augment > 0 :
        visited = [False for i in range(len(availability))]
        bottlenck = float('inf')
        augment = dfs(availability,0,10,bottlenck,visited)
        flow += augment
    return flow
def dfs(g:list,s,e,bottleneck,visited):
    """
    Implementation of dfs with modification for to suit into the purpose of running Ford Fulkerson, the function
    will go through the every possible edges until it reach the reach the super sink destination, on the way going there
    it will recorded the amount of flow that every edges are capable with, after reaching the sink, it will return the
    flow, and modifying the flow of each edges accordingly, and also return the flow for it able to bump through.
    :Input:a adjacency list Residual network flow graph for the given time table(availability), location of super source
    , location of super sink, bottleneck which is the capable flow, visisted list
    argv1: g for a adjacency list Residual network flow graph for the given time table(availability)
    argv2: s for location of super source
    argv3: e for location of super sink
    argv4: bottleneck for capable flow
    argv5: visited for visisted list
    :Output, return or postcondition: maximum capable flow going from sources to sink, and also modifying the graph
                                        according by the capable flow
    :Time complexity: travel through the list, which will cost O(V+E) in the worst, but we know that by the
                        characteristic of our input, it will take O(n) to traverse through the entire list because
                        the size of the list we input is O(n)
                        where n is the number of days.
    :Aux space complexity: getting visited lst in the input will have O(n) where n is the number of day
                            -> also we are getting the input of a adjacency list Residual network
                            flow graph for the given time table(availability) which have over space complexity of O(n)
                            ->therefore the overall space complexity will be O(n)
    """
    if s == e:
        return bottleneck
    visited[s] = True
    for edges in g[s]:
        residual = edges.reverse.see_edge()[1]
        if residual > 0 and not visited[edges.see_edge()[0]]:
            augment = dfs(g,edges.see_edge()[0],e,min(bottleneck,residual),visited)
            if augment > 0:
                edges.see_edge()[1] += augment
                edges.reverse.see_edge()[1] -= augment
                return augment
    return 0
def allocate(availability):
    """
    a function for preparing the schedule of who is responsible for preparing each meal in the
    next n days (numbered 0, 1, . . . , n − 1) for the 5 housemates , with the help of adj_list function to generate a
    adjacency list Residual network flow graph for the given time table(availability). Then applied the Ford_fulkerson
    on that graph, to find the maximum flow bump through the entire graph and also finding the path for that max flow.
    returning the time table for all five house members for the next n days.
    :Input:a list of lists availability for each person each day
            For a person numbered j and day numbered i, availability[i][j] is equal to:
            0, if that person has neither time availability to prepare the breakfast nor the dinner
            during that day.
            if that person only has time availability to prepare the breakfast during that day.
            if that person only has time availability to prepare the dinner during that day.
            if that person has time availability to prepare either the breakfast or the dinner during
            that day.
    argv1:availability : a list of lists availability for each person each day
    argv2:
    :Output, return or postcondition:   returns (breakfast, dinner), where lists breakfast and dinner specify a
    valid allocation. breakfast[i] = j if person numbered j is allocated to prepare breakfast
    on day i, otherwise breakfast[i] = 5 to denote that the breakfast will be ordered from
    a restaurant on that day. Similarly, dinner[i] = j if person numbered j is allocated to
    prepare dinner on day i, otherwise dinner[i] = 5 to denote that the dinner will be ordered
    from a restaurant on that day.
    :Time complexity: The highest time complexity for this function is calling ford_fulkerson which is O(n^2)
                        -> overall complexity is O(n^2)
    :Aux space complexity: complexity of initialise morning is O(n) and night is O(n) where n the number of days
                           also highest space is calling either ford_fulkerson and adj_list are O(n).
                           -> O(n)
    """
    graph = adj_list(availability)
    if ford_fulkerson(graph) < len(availability)*2:
        return None

    morning = [None for i in range(len(availability))]
    night = [None for i in range(len(availability))]
    for i in range(3, 9, 1):
        for edges in graph[i]:
            day = edges.see_edge()[0]
            if day < 10:
                continue
            elif (day - 10) % 4 == 1 and (edges.see_edge()[1] == 1):
                morning[(day-10)//4] = i-3
            elif (day - 10) % 4 == 2 and (edges.see_edge()[1] == 1):
                night[(day-10)//4] = i-3
            elif (day - 10) % 4 == 3 and (edges.see_edge()[1] == 1):
                if morning[(day-10)//4] is None:
                    morning[(day - 10) // 4] = i - 3
                elif night[(day-10)//4] is None:
                    night[(day - 10) // 4] = i - 3
                else:
                    morning[(day - 10) // 4] = i - 3
                    night[(day - 10) // 4] = i - 3
    return (morning,night)


if __name__ == '__main__':
    availability = [[2, 0, 2, 1, 2], [3, 3, 1, 0, 0],
                    [0, 1, 0, 3, 0], [0, 0, 2, 0, 3],
                    [1, 0, 0, 2, 1], [0, 0, 3, 0, 2],
                    [0, 2, 0, 1, 0], [1, 3, 3, 2, 0],
                    [0, 0, 1, 2, 1], [2, 0, 0, 3, 0],
                    [2, 0, 2, 1, 2], [3, 3, 1, 0, 0],
                    [0, 1, 0, 3, 0], [0, 0, 2, 0, 3],
                    [0, 1, 0, 3, 0], [0, 0, 2, 0, 3],
                    [0, 1, 0, 3, 0], [0, 0, 2, 0, 3],
                    [0, 1, 0, 3, 0], [0, 0, 2, 0, 3],
                    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
                    ]
    print(allocate(availability))
