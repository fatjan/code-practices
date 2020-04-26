class Abc:
    def method123(self, text):
        print('Hello, ', text)
        MainApp.method456(self, 'kamu')
    

class MainApp:

    def method456(self, x):
        Abc.method123(self, x)
    
    def method789(self):
        self.method456('Hello World!')
        KelasAtas.methodAtas(self,'Kamu')

kucing = MainApp()
kucing.method789()
