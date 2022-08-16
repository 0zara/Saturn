import imgbbpy, pickle

def imglog(imglink):
    client = imgbbpy.SyncClient('32807022e1c707416d5f1ce6faf891c7')
    image = client.upload(url=imglink)
    pickle_out = open("dict.pickle","wb")
    link=image.url
    pickle.dump(link, pickle_out)
    pickle_out.close()
        
    

