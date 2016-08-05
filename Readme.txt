***Running instructions***
1. sudo sparse run (This will fail saying the program could not find a log file)
2. sudo lein run -m streamparse.commands.run/-main topologies/tweetwordcount.clj -t 120 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path=/home/janson/EX2Tweetwordcount/logs' --option 'streamparse.log.level="debug"'


For some reason, following the instructions given does not produce a working program. 
"sparse run" is needed to generate the _resource folder but for some reason it will 
fail due to it not finding a log file. The second command is actually the command 
that pops up after "sparse run" is entered. The only difference is that 
the "streamparse.log.path=/home/janson/EX2Tweetwordcount/logs" has quotes around it, 
so it cannot be found. 

After removing the added quotes and entering the command manually, the program works!


**Instructions for scripts**

1. finalresults.py: "sudo python finalresults.py <word>"
#this script is to query how many times a word has came up during the twitter stream.

2. finalresults.py: "sudo python finalresults.py"
#if a word is not passed in, the script will print out the whole table.

3. histogram.py: "sudo python histogram.py <minimum number, maximum number>"
#this will print out words within the range of the numbers passed through.
