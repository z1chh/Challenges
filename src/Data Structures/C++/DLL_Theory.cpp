#include <iostream>
#include "Node.cpp"
#include "DLL.cpp"

using namespace std;

int main()
{
    int array[8] = {2, 4, 7, 7, 11, 12, 13, 26};
    DLLStructure dll = DLLStructure(array, 8);

    // Q11 theory question
    // print to the screen the written answer for the theory question
    cout << endl
         << "Question 11 Theory Question:" << endl;
    cout << "I  implemented GetMax()  and GetMin()  by  iterating through every Node, and  then finding  the highest  and lowest" << endl;
    cout << "values.  However, if  these  two  methods were  called  often,  rather than  doing  what  I  implemented, it  would" << endl;
    cout << "be more efficient  for them to call  Sort(), and  then simply call and return  the value of GetTail() and GetHead()" << endl;
    cout << "respectively. Inversely, if we rarely use these methods, then it would be more efficient to keep my implementation." << endl;

    // Q12 theory question
    cout << endl
         << endl
         << "Question 12 Theory Question:" << endl;
    // print to the screen the written answer for the theory question
    cout << "The  default copy constructor that is  provided by  the  compiler will  perform a shallow copy  rather than a  deep" << endl;
    cout << "copy.  In other  words,  we will have a  new DLLStructure  object,  but that its  parameters,  even though they are" << endl;
    cout << "different pointer objects,  will still point to  the same Nodes  (aFirst and aLast),  which themselves point to the" << endl;
    cout << "same Nodes (i.e. both DLLStructures share the same list). Similarly, any Node of that DLLStructure will be the same" << endl;
    cout << "Node  objects as  the original DLLStructure. Therefore,  this destroys the encapsulation and provides data leaking." << endl;
    cout << "For  example,  a  user  can  modify or  even  delete  Nodes  of  the new  DLLStructure by  modifying  the  original" << endl;
    cout << "DLLStructure.  Inversely, any  modifications made  to  the new  DLLStructure  can  be  seen  through  the  original" << endl;
    cout << "DLLStructure. A better copy constructor would be make a deep copy of the initial DLLStructure and create new Nodes." << endl;

    // Q12
    cout << endl
         << "Question 12:" << endl;
    DLLStructure dll2(dll);
    dll2.PrintDLL(); // the output should be: 2, 4, 7, 7, 11, 12, 13, 26
}