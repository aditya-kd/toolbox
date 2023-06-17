#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
    string word;
    string sentence;
    int age;
    float fnum;
    double dnum;

    int size = 5;
    vector<int> arr;
    vector<int> arr2(size);
    vector<int> arr3(size, 18);

    cin>>word;
    scanf("%s", sentence);
    cin>>age;
    cin>>fnum;
    cin>>dnum;

    int x;
    for(int i=0;i<size;i++){
        cin>>x;
        arr.push_back(x);
    }
    // Using size variable
    for(int i=0;i<size;i++){
        cin>>x;
        arr2[i] = x;
    }
    
    //printing
    cout<<"Word "<<word<<endl;
    cout<<"Sentence "<<sentence<<endl;
    cout<<"Age "<<age<<endl;
    cout<<"Float "<<fnum<<endl;
    cout<<"Double "<<dnum<<endl;
    cout<<"Array "<<endl;
    
    for(int i =0;i<size;i++){
        cout<<arr[i]<<" ";
    }cout<<endl;


    
}