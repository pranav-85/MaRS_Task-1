#include<iostream>
using namespace std;
int main(){

    auto val = "Sai Pranav";
    auto var = [&]{
        return val;
    }();

    cout << var;
}