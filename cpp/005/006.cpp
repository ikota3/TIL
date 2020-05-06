int main()
{
    double height{};
    std::cout << "Enter height(m): "s;
    std::cin >> height;

    double weight{};
    std::cout << "Enter weight(kg): "s;
    std::cin >> weight;

    double bmi = weight / (height * height);
    std::cout << "BMI is "s << bmi << std::endl;
}