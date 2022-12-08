#include <bits/stdc++.h>
#include <vector>
#include <iostream>

int main(){
    int find_num;
    std::cout << "Enter numbr to find: ";
    std::cin >> find_num;
    std::vector <int> num {1, 2, 3, 4, 5};
    std::vector <int> ::iterator iter;
    std::cout << "Original Vector";
    for (int i = 0; i < num.size(); i++)
    {
        std::cout << num[i] << " ";
    }
    std::cout << "\n";
    iter = std::find(num.begin(), num.end(), find_num);
    if(iter != num.end()){
        std::cout << "Element " << find_num << " found at positiin: ";
        std::cout << (iter - num.begin()) + 1 << "\n";
    }
    else{
        std::cout << "Element " << find_num << " not found.\n";
    }
}