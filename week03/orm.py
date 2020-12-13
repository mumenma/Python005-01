from enum import unique
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData, engine,desc,func,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class Person_table(Base):
    __tablename__ = 'person'
    id = Column(Integer(),primary_key = True,autoincrement=False)#primary_key 表示是否是主键  autoincrement表示是否是自动增长
    user_name = Column(String(20),nullable = False,unique=True)# unique 表示是否是唯一  nullable表示是否可以为空
    age = Column(Integer)
    birthday = Column(Integer)
    sex = Column(Integer)
    education = Column(String(20))
    create_date = Column(DateTime(), default=datetime.now) # default 表示默认的值
    update_date = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
if __name__ == "__main__":    
    dburl = "mysql+pymysql://root:******@127.0.0.1:3306/testdb"
    engine = create_engine(dburl, echo=True)

    metadata = MetaData(engine)

    # 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
    # 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
    # 将 ORM、插入、查询语句作为作业内容提交
    person_table = Table('person',metadata,
        Column('id',Integer,primary_key = True),
        Column('user_name',String(20)),
        Column('age',Integer),
        Column('birthday',Integer),
        Column('sex',Integer),
        Column('education',String(20)),
        Column('create_date',DateTime(), default=datetime.now),
        Column('update_date',DateTime(), default=datetime.now,
                            onupdate=datetime.now))
    try:
        metadata.create_all()
    except Exception as e:
        print(f"create error {e}")

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    person1 = Person_table(id=1,user_name = "姓名1",age=30,birthday=815,sex=1,education="本科")
    person2 = Person_table(id=2,user_name = "姓名2",age=31,birthday=816,sex=1,education="本科")
    person3 = Person_table(id=3,user_name = "姓名3",age=32,birthday=817,sex=2,education="博士")
    session.add(person1)
    session.add(person2)
    session.add(person3)

    query = session.query(Person_table.user_name,Person_table.id).order_by(desc(Person_table.id)).limit(2)
    print([result.user_name for result in query])


    result = session.query(func.count(Person_table.user_name)).first()
    print(result)

    query2 = session.query(Person_table).filter(or_( Person_table.id < 2,Person_table.sex == 2))
    print([result.user_name for result in query2])

    query3 =  session.query(Person_table).filter(Person_table.id == 2)
    query3.update({Person_table.user_name:"学员20"})
    new_person= query3.first()
    print(new_person.user_name)

    query4 = session.query(Person_table).filter(Person_table.id == 1)
    # session.delete(query4.one())
    query4.delete()#上面的那个语句同样可以

    session.commit()



