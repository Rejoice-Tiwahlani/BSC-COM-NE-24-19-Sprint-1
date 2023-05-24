REPORT DETAILING SIGNIFICANT OBSERVATIONS MADE FROM THE TWO IMPLEMENTATIONS

The thread pool is more efficient to use when it has to service a larger number of clients as 
compared to the one demand privision which should more preferably be used when there is need to service fewer clients.

In the concurrent server,several clients were able to connect and send messages at the same time whilst in the threadpool server
implemenation,the sever communicates with only the specific number of clients which is 10 in this case, if there happens that
any new incoming connection arrrives or is requested, the server simply just accepts the connection but does not allow the
clients to send messages to the server(since all the threads are being used which mplies that there are no resources to service
the particular connetion.

Using a threadpool howwever comes in handy because it enables and allows us to reuse threads which means that resources are alos reused
hence leading to resource utilization in the long run. It also speeds up performance since clients that want to connect do not have to wait 
for a long time in the queue before their request is satisfied by the 

In conclusion, threads are a good approach in programming but just as any programming paradigm, also has its downfalls here and there.They most
importantly improve the overall perfromsnce of the system as a whole.
