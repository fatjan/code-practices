#include <stdio.h>
#include <math.h>
#define PI 3.141593

int main()
{   
    int t,a,H,THETA_MAX,i,h;
    float vol_temp,b_temp,h_temp;

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d %d %d",&a,&H,&THETA_MAX);
       
        if(THETA_MAX==0) h=H;
       
        else if(H/tan(THETA_MAX*PI/180)>a){
           
            vol_temp=0.5*H*H/tan(THETA_MAX*PI/180);
            b_temp=H/tan(THETA_MAX*PI/180)-a;
            h_temp=tan(THETA_MAX*PI/180)*b_temp;
            h=ceil((vol_temp-0.5*b_temp*h_temp)/a);
        }
        else {
           
            vol_temp=0.5*H*H/tan(THETA_MAX*PI/180);
            h=ceil(vol_temp/a);
        }

        printf("%d\n",h);
    }
    return 0;
}