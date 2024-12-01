#include <iostream>
using namespace std;

int NAND(int A, int B) {
    return !(A && B);  // NAND Operation
}

int main() {
    int A, B;
    cout << "Masukkan nilai A (0 atau 1): ";
    cin >> A;
    cout << "Masukkan nilai B (0 atau 1): ";
    cin >> B;

    cout << "NAND Gate: " << NAND(A, B) << endl;

    return 0;
}
