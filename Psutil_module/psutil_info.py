import psutil
import cpuinfo


cpu_info = cpuinfo.get_cpu_info()
print(f"Full CPU Info:{cpu_info['brand_raw']}")
print(f"Actual Hz:{cpu_info['hz_actual_friendly']}")
print(f"Advertised Hz:{cpu_info['hz_advertised_friendly']}")


#CPU count ( No of CPU ):
cpu_count=psutil.cpu_count()
print(f"CPU count:{cpu_count}")
#CPU usage:
cpu_usage=psutil.cpu_percent()
print(f"Cpu usage:{cpu_usage} %")

#Memory:
memory=psutil.virtual_memory()
print(f"Total RAM Memory:{int(memory.total)/1024 /1024/1024:.2f} GB")
print(f"Available Memory:{int(memory.available)/1024 /1024/1024:.2f} GB")
print(f"Usage Percentage:{memory.percent} %")

#Network information:(ADDITIONAL INFORMATION)
network=psutil.net_io_counters()
print(f"Bytes sent:{network.bytes_sent}")
print(f"Bytes received:{network.bytes_recv}")

#see process running and can be used to trigger a specific task when an app is launched:
processes = psutil.process_iter()
for process in processes:
    process_name = process.name()
    print(f"Process:{process_name}")






