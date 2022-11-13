from database import Thread

# Thread.create(name="Keisuke",title="Title",body="Body")
threads = Thread.select()
# thread01 = Thread(name="keisuke01", title="Title01",body="Body01")
# thread01.save()
print(threads[0].name)
print(threads[2].name)

threads = Thread.select().where(Thread.name == "keisuke01").get()
print(threads.name,threads.title,threads.body)
