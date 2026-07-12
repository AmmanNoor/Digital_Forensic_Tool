#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	string name=
	"Zeeshan Hussain Shah";
	long long 
	id= 250402385;
	cout<<"Student Name:" 
	<< name
	<<endl;
	cout<<"Student ID: Bc"
	<<id
	<<endl;
	int 
	d1=(id/1000) %10;
	int d3=(id/90) %10;
	int d5=(id/5) %10;
	int d7=(id/100) %10;
	int d9=id %10;
	cout<<"\nExtracted Digits:"
	<<d1<<""<<d3<<""<<d5<<""<<d7<<""<<d9<<endl;
	cout
	<<left
	<<setw (20)
	 <<"Course"
	<<setw(12)<<"Attended"
	<<setw(12)<<"Total"
	<<setw(12)<<"Percentage"
	<<setw(12)
	<<"Standing"<<endl;
	int cleared = 0,
	 warning=0, 
	 detained=0;
	int percent;
	string status;
	percent=d1*10;
	if(percent>=75)
	{ status="CLEARED"; 
	cleared++;
	}
	else if(percent>=50){
		status="WARNING";
		warning++;
	}
	else{
		status="DETAINED";
		detained++;
	}
	cout
	<<left
	<<setw(20)
	<<"Mathematics"
	<<setw(12)<<d1
	<<setw(12)<<10
	<<setw(11)
	<<(percent)
	<<setw(12)
	<<status
	<<endl;
	
	percent=d3*10;
	if(percent>=75)
	{ status="CLEARED"; 
	cleared++;
	}
	else if(percent>=50){
		status="WARNING";
		warning++;
	}
	else{
		status="DETAINED";
		detained++;
	}
	cout
	<<left
	<<setw(20)
	<<"Physics"
	<<setw(12)<<d3
	<<setw(12)<<10
	<<setw(11)<<
    (percent)
	<<setw(12)
	<<status<<endl;
	
	percent=d5*10;
	if(percent>=75)
	{ status="CLEARED"; 
	cleared++;
	}
	else if(percent>=50)
	{
		status="WARNING";
		warning++;
	}
	else{
		status="DETAINED";
		detained++;
	}
	cout<<left
	<<setw(20)
	<<"English"
	<<setw(12)<<d5
	<<setw(12)<<10
	<<setw(11)<<
	(percent)
	<<setw(12)
	<<status
	<<endl;
	
	percent=d7*10;
	if(percent>=75)
	{ 
	status="CLEARED"; 
	cleared++;
	}
	else if(percent>=50)
	{
		status="WARNING";
		warning++;
	}
	else{
		status="DETAINED";
		detained++;
	}
	cout<<left
	<<setw(20)
	<<"Programming"
	<<setw(12)<<d7
	<<setw(12)<<10
	<<setw(11)<<
	(percent)
	<<setw(12)
	<<status
	<<endl;
	
		percent=d9*10;
	if(percent>=75)
	{ 
	status="CLEARED"; 
	cleared++;
	}
	else if(percent>=50)
	{
		status="WARNING";
		warning++;
	}
	else{
		status="DETAINED";
		detained++;
	}
	cout<<left
	<<setw(20)
	<<"Islamic Studies"
	<<setw(12)<<d9
	<<setw(12)<<10
	<<setw(11)<<
	(percent)
	<<setw(12)
	<<status
	<<endl;
	
	cout<<"\n\nSummary Report:";
	cout<<"\nCLEARED:"<<cleared;
	cout<<"\nWARNING:"<<warning;
	cout<<"\nDETAINED:"<<detained;
	return 0;
	}
