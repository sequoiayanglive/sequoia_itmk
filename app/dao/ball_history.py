from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Ball_history(Base):
    __tablename__ = 'ball_history'
    id = Column(Integer, primary_key=True)
    issue = Column(Integer)
    red1 = Column(Integer)
    red2 = Column(Integer)
    red3 = Column(Integer)
    red4 = Column(Integer)
    red5 = Column(Integer)
    red6 = Column(Integer)
    blue = Column(Integer)

    def __repr__(self):
        tpl = "ball_history(id={},issue={},red1={},red2={},red3={},red4={},red5={},red6={},blue={})"
        return tpl.format(self.id
                          , self.issue
                          , self.red1
                          , self.red2
                          , self.red3
                          , self.red4
                          , self.red5
                          , self.red6
                          , self.blue )