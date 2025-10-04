import socket
from concurrent.futures import ThreadPoolExecutor

class port_scanner():
    def _init_(self):
        pass
    
    @staticmethod
    def port_scanner(target, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                
                result = s.connect_ex((target, port))
                
                if result==0:
                    print(f"port:{port} is open")
                    
                elif result in [111, 113]:
                    print (f"Port: {port} is Closed")
                    
                else:
                    print(f"Port: {port} is Filtered")
            
        except Exception as e:
            print (f"Exception error: {e}")
    
    def reader(target, thread_count=500):
        ports = range (1,1024)
        
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            for port in ports:
                executor.submit(port_scanner.port_scanner, target, port)
        executor.shutdown(wait=True)
        
        print("Port Scan Completed!!")
        
    def mN():
        
        choice= input("Enter target domain:").strip().lower()
        target=socket.gethostbyname(choice)
        port_scanner.reader(target=target)
        
if __name__=="__main__":
    port_scanner.mN()
    