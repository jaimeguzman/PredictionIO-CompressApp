"""

"""

import predictionio
import argparse
import time


# def import_events(client, file):
def checker(client, file):
  f = open(file, 'r')
  count = 0
  print "Importando la DATA..."
  for line in f:
    data = line.rstrip('\r\n').split(" ")
    # data.remove('')

    # print data
    cliente = client  
    pos = 0
    for features in data:
      # print "El usuario %d vio la pagina %s por %d vez " % (count,features, pos)
      #time.sleep(3) # delays for 5 seconds
      for ft in features:
        pos += 1
        # cliente.create_event(
        #   event="view",   #el usuario siempre ve una seccion de PRISA
        #   entity_type="user",
        #   entity_id=str(count), # use the count num as user ID
        #   properties= {
        #     "page" : ft,
        #     "pos" :  int(pos)
        #   }
        # )
        print "entity_id:    %d \t  <feature, pos> == <%s,%d>" % (count,ft,pos )

    count += 1
  f.close()
  print "%s events are imported." % count




if __name__ == '__main__':

  parser.add_argument('--file',       default="./data/msnbc990928-letter-split10.seq")
  args = parser.parse_args()
  print args

