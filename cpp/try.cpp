int Reverse(int num) 
{ 
    int rev_num = 0; 
    if (num > 0){
        while(num > 0) 
        { 
            rev_num = rev_num*10 + num%10; 
            num = num/10; 
        } 
        return rev_num; 
    }   else {
        number = abs(num)
        while(number > 0) 
        { 
            rev_num = rev_num*10 + number%10; 
            number = number/10; 
        } 
        return rev_num*(-1); 
    }
} 
  