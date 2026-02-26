class Pc:
    def __init__(self, cpu, gpu, ram, rom):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.rom = rom

    def bukaCyberpunk(self):
        print("NGUNGGGGGG (bunyi kipas)")
    
    def gantiCpu(self, cpuBaru):
        self.cpu = cpuBaru
    
pc1 = Pc("Ryzen 9", "Rtx 6090", "64 GB", "2 TB")
pc2 = Pc("Pentium", "Gtx 750", "4 GB", "64 GB")
pc3 = Pc("Intel core i5", "Gtx 1080 TI", "16 GB", "1 TB")

pc1.bukaCyberpunk()

print(f"Sebelum diubah pc2 prosesornya {pc2.cpu}")
pc2.gantiCpu("Intel core i9")
print(f"Sekarang pc 2 prosesornya {pc2.cpu}")

