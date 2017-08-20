#include<iostream>
using namespace std;

int main()
{
// n1, n2 and n3 are the money values of coins of type 1,2 and 3 respectively
int n1=1;
int n2=10;
int n3=15;
int total=100;
// c1,c2,c3 are the number of coins of type 1,2,3 respectively
int count,c1,c2,c3,c;
c1=0;c2=0;c3=0;
int temp=total;
//count = total coins
count=0;
if(temp%n3==0)
{
count=temp/n3;
}
else if(temp%n2==0)
{
  
count=temp/n2;
}
else if(temp%n1==0)
{
count=temp/n1;
}
c1=c1+temp/n3;
temp=temp-(c1*n3);
if(temp!=0)
{
c2=c2+temp/n2;
temp=temp-(c2*n2);
}
if(temp!=0)
{
c3=c3+temp/n1;
temp=temp-(c1*n1);
}
c=c1+c2+c3;
if(c<count)
cout<<c;
else 
cout<<count;

return 0;
}
