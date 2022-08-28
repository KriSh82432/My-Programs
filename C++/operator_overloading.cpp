#include <iostream>
using namespace std;

class Box
{
private:
    float height,length,breadth,volume;
public:
    float getVolume(void){
        return height *length *breadth;
    }
    void setHeight(float x){
        height = x;
    }
    void setBreadth(float y){
        breadth = y;
    }
    void setLength(float z){
        length = z;
    }
    Box operator +(const Box &b){
        Box box;
        box.length = this->length + b.length;
        box.breadth = this->breadth + b.breadth;
        box.height = this->height + b.height;
        return box;
    }
};

int main(){
    Box Box1;
    Box Box2;
    Box Box3;
    float vol1, vol2, vol3;
    Box1.setHeight(25.0);
    Box1.setBreadth(25.0);
    Box1.setLength(25.0);
    Box2.setHeight(10.0);
    Box2.setBreadth(10.0);
    Box2.setLength(10.0);
    Box3 = Box1.operator +(Box2);
    vol1 = Box1.getVolume();
    vol2 = Box2.getVolume();
    vol3 = Box3.getVolume();
    cout << "Volume of Boxes :" << endl
         << "1. " << vol1 << endl
         << "2. " << vol2 << endl
         << "3. " << vol3 << endl;
    return 0;
}