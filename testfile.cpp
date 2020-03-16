#include <iostream>
#include <fstream>

int main()
{
    const char *fileName = "/pwd/testfile.txt";

    std::ofstream ofs(fileName);
    if (!ofs)
    {
        std::cout << "ファイルが開けませんでした。" << std::endl;
        std::cin.get();
        return 0;
    }

    ofs << "あいうえお　かきくけこ" << std::endl;
    std::cout << fileName << "に書き込みました。" << std::endl;

    std::cin.get();
}