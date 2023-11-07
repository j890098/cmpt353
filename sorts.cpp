#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <time.h>
#include <chrono>
#include <algorithm>
#include "paramobj.hpp"

using namespace std;
using namespace std::chrono;
int main(int argc, char * argv[])
{
    
    fstream myfile("parameters.txt", std::ios_base::in);

    int i=0;
    int readInt;
    int readInts[2];

    while (myfile >> readInt)
    {
        if(i<2){
            readInts[i]=readInt;
            i++;
        }
    }
    Param params = Param(readInts[0],readInts[1]);
    cout << "N=" << params.N <<" ARRAY_SIZE= "<< params.ARRAY_SIZE << endl;

    srand(time(NULL));
    vector<int> randArr;
    vector<int> result;
    vector<int> resultComparison;
    milliseconds start;
    milliseconds end;

    for(int i=0;i<params.N;i++){
        for(int j=0;j<params.ARRAY_SIZE;j++){
            randArr.push_back(rand());
        }
        start = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        sort (randArr.begin(), randArr.end());
        end = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        result.push_back((end-start).count());
        start = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        sort (randArr.begin(), randArr.end(), greater<int>());
        end = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        resultComparison.push_back((end-start).count());
        randArr.clear();
    }
    
    // cout << "timed " << (end-start).count() << endl;
    ofstream outCSV("c_data.csv");
    outCSV << "c_builtin,c_builtin_greaterthan" << endl;
    for(int i=0;i<params.N;i++){
        outCSV << result.back() << "," << resultComparison.back() << endl;
        result.pop_back();
        resultComparison.pop_back();
    }
    outCSV.close();
    return 0;
}