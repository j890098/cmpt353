#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <time.h>
#include <chrono>
#include <iterator>
#include <algorithm>
#include "paramobj.hpp"
#include <cassert>


using namespace std;
using namespace std::chrono;

void swap(vector<int>& v, int x, int y);

void impquicksort(vector<int> &vec, int start, int end) {
    int i = start;
    int j = end;

    int pivotIndex = start + rand()%(end-start);
    int pivot = vec[pivotIndex];
    
    while (i<end || j>start) {
        while (vec[i] < pivot)
            i++;
        while (vec[j] > pivot)
            j--;

        if (i <= j) {
            swap(vec, i, j);
            i++;
            j--;
        }
        else {
            if (i < end)
                impquicksort(vec, i, end);
            if (j > start)
                impquicksort(vec, start, j);
            return;
        }
    }
}

void swap(vector<int>& v, int x, int y) {
    int temp = v[x];
    v[x] = v[y];
    v[y] = temp;
}


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
    int result;
    int resultComparison;
    int resultQuicksort;
    milliseconds start;
    milliseconds end;


    ofstream outCSV("c_data.csv");
    outCSV << "c_builtin,c_builtin_greaterthan,c_quicksort" << endl;
    for(int i=0;i<params.N;i++){
        for(int j=0;j<params.ARRAY_SIZE;j++){
            int generated = rand();
            randArr.push_back(generated);
        }
        
        start = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        sort (randArr.begin(), randArr.end());          // builtin sort
        end = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        result = (end-start).count();
        start = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        sort (randArr.begin(), randArr.end(), greater<int>());  // builtin sort with > parameter
        end = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        resultComparison = (end-start).count();
        start = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        impquicksort (randArr, 0, params.ARRAY_SIZE-1);  // coded quicksort
        end = duration_cast< milliseconds >(
            system_clock::now().time_since_epoch()
        );
        // cout << "iteration" << i << endl;
        outCSV << result << "," << resultComparison <<  "," << resultQuicksort << endl;
        resultQuicksort = (end-start).count();
        randArr.clear();
    }
    
    // cout << "timed " << (end-start).count() << endl;
    // ofstream outCSV("c_data.csv");
    // outCSV << "c_builtin,c_builtin_greaterthan,c_quicksort" << endl;
    // for(int i=0;i<params.N;i++){
    //     outCSV << result.back() << "," << resultComparison.back() <<  "," << resultQuicksort.back() << endl;
    //     result.pop_back();
    //     resultComparison.pop_back();
    //     resultQuicksort.pop_back();
    // }
    outCSV.close();
    return 0;
}