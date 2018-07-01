from app import db

class Song(db.Model):

    __tablename__ = 'song'

    id = db.Column(db.String(32),primary_key = True)
    filename = db.Column(db.String(128))
    filehash = db.Column(db.String(64))
    albumid =  db.Column(db.String(32))
    singername = db.Column(db.String(32))
    songname = db.Column(db.String(128))
    albumname = db.Column(db.String(64))
    play_url = db.Column(db.String(128))
    lyrics = db.Column(db.Text())
    img_url = db.Column(db.String(128))

    def __init__(self,id,filename,filehash,albumid,singername,songname,albumname,play_url,lyrics,img_url):
        self.id = id
        self.filename = filename
        self.filehash= filehash
        self.albumid = albumid
        self.singername = singername
        self.songname = songname
        self.albumname = albumname
        self.play_url = play_url
        self.lyrics = lyrics
        self.img_url = img_url

    def __repr__(self):
        return "{0}:{1} -- {2} URL:{3}".format(self.singername,self.songname,self.albumname,self.play_url)

    def save(self):
        try:
            this = Song.query.get(self.id)
            if this:
                this.filename = self.filename  
                this.filehash =  self.filehash
                this.albumid =  self.albumid 
                this.singername = self.singername
                this.songname = self.songname 
                this.albumname = self.albumname  
                this.play_url = self.play_url  
                this.lyrics = self.lyrics 
                db.session.add(this)
            else:
                db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Error:"+str(e))
            db.session.rollback()
    
    def toJson(self):
        print(self.songname)
        return {
            'title': self.songname,
            'author' : self.singername,
            'url': self.play_url,
            'lrc': self.lyrics,
            'pic': self.img_url,
        }
