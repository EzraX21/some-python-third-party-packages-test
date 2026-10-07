from faker import Faker
from tqdm import trange
fake = Faker()
datas = []
with open("./documents/outputs/datas.txt","a") as f:
    f.write("name,email,job\n")
    for _ in trange(5):
        data = fake.name()+","+fake.email()+","+fake.job()+"\n"
        f.write(data)