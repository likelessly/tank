#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
void AddStudent();
void DisplayStudent();
void AverageStudent();
void DisplayGrade();
string CalculateGrade(float total);
int main()
{
    fstream File;
    string ID, Name;
    int choice = -1, test1, test2, test3;
    float total;
    do
    {
        system("cls");
        cout << "Program Add Student Data\n";
        cout << "Main Menu\n";
        cout << "0 - Exit\n";
        cout << "1 - Add Student\n";
        cout << "2 - Display Student Data\n";
        cout << "3 - Display Average Score\n";
        cout << "4 - Display Grade Score\n";
        cout << "Select Choice : ";
        cin >> choice;
        if (choice == 1) AddStudent();
        else if (choice == 2) DisplayStudent();
        else if (choice == 3) AverageStudent();
        else if (choice == 4) DisplayGrade();
    } while (choice != 0);
    return 0;
}

void AddStudent()
{
    fstream File;
    string ID, Name;
    int test1, test2, test3;
    cout << "Enter ID : ";
    cin >> ID;
    cout << "Enter Name : ";
    cin >> Name;
    cout << "Enter Test 1 (0-100): ";
    cin >> test1;
    cout << "Enter Test 2 (0-100): ";
    cin >> test2;
    cout << "Enter Test 3 (0-100): ";
    cin >> test3;
    File.open("Student.dat", ios::out | ios::app);
    if (File.is_open()){
        File << endl << ID << " " << Name << " " << test1 << " " << test2 << " " << test3;
        cout << "Saved\n";
    }
    else cout << "File is not Opened\n";
    File.close();
    cout << "Data Students\n";
    cout << ID << " " << Name << " " << test1 << " " << test2 << " " << test3 << endl;
    system("pause");
}

void DisplayStudent()
{
    fstream File;
    string ID, Name;
    int test1, test2, test3;
    File.open("Student.dat", ios::in);
    cout << "List Students\n";
    cout << "ID\t" << "Name\t\t" << "Test1\t" << "Test2\t" << "Test3\t" << endl;
    while(File.eof() != true){
        File >> ID >> Name >> test1 >> test2 >> test3;
        cout << fixed;
        cout << ID << "\t" << Name << "\t\t" << setprecision(2) << (float)test1 << "\t" << (float)test2 << "\t" << (float)test3 << endl;
    }
    File.close();
    system("pause");

}

void AverageStudent()
{
    fstream File;
    string ID, Name;
    int test1, test2, test3, no = 1;
    File.open("Student.dat", ios::in);
    cout << "List Students\n";
    cout << "No.\t" << "ID\t" << "Name\t\t" << "Test1(25%)\t" << "Test2(25%)\t" << "Test3(50%)\t" << "Total(100%)\t" << endl;
    while(File.eof() != true){
        File >> ID >> Name >> test1 >> test2 >> test3;
        cout << fixed;
        float total = ((float)test1 * 25 + (float)test2 * 25 + (float)test3 * 50) / 100;
        cout << no << "\t" << ID << "\t" << Name << "\t\t" << setprecision(2) << (float)test1 * 25 / 100 << "\t\t" << (float)test2 * 25 / 100 << " \t\t" << (float)test3 * 50 / 100 << "\t\t";
        cout << total << endl;
        no++;
    }
    File.close();
    system("pause");
}

void DisplayGrade()
{
    fstream File;
    string ID, Name;
    int test1, test2, test3, no = 1;
    File.open("Student.dat", ios::in);
    cout << "List Students\n";
    cout << "No.\t" << "ID\t" << "Name\t\t" << "Total\t" << "Grade" << endl;
    while(File.eof() != true){
        File >> ID >> Name >> test1 >> test2 >> test3;
        cout << fixed;
        float total = (test1 * 25 + test2 * 25 + test3 * 50) / 100;
        cout << no << "\t" << ID << "\t" << Name << "\t\t" << setprecision(2) << total << "\t" << CalculateGrade(total) << endl;
        no++;
    }
    File.close();
    system("pause");
}

string CalculateGrade(float total)
{
    if (total >= 80) return "A";
    else if (total >= 75) return "B+";
    else if (total >= 70) return "B";
    else if (total >= 65) return "C+";
    else if (total >= 60) return "C";
    else if (total >= 55) return "D+";
    else if (total >= 50) return "D";
    else return "F";
}



