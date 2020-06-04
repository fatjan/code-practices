class Repository {       
    private:            
        char32_t itemName;  
        char32_t itemContent;
        int itemType;      
        // this->radius
    public:
        Repository(char32_t itemNameInput, char32_t itemContentInput, int itemTypeInput) { // Constructor with parameters
        itemName = itemNameInput;
        itemContent = itemContentInput;
        itemType = itemTypeInput;
        }
        void Register(char32_t itemNameInput, char32_t itemContentInput, int itemTypeInput){
            itemName = itemNameInput;
            itemContent = itemContentInput;
            itemType = itemTypeInput;
        }
        void Retrieve(char32_t itemNameInput){
            return ''
        }
        void GetType(char32_t itemNameInput){
            return ""
        }
        void Deregister(char32_t itemNameInput){
            return ""
        }
};