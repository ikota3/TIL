int main()
{
    // BMI = weight(kg) / (height(m) ^ 2)
    double height = 1.6;
    double weight = 50.0;
    double bmi = weight / (height * height);

    std::cout << "BMI is "s << bmi << std::endl;

    auto bmiStatus = [](auto bmi) {
        std::string bmiResult{};
        if (bmi < 18.5)
        {
            bmiResult = "Underweight";
        }
        else if (bmi < 25)
        {
            bmiResult = "Normal";
        }
        else if (bmi < 30)
        {
            bmiResult = "Overweight";
        }
        else
        {
            bmiResult = "Obese";
        }
        std::cout << "BMI result is "s << bmiResult << std::endl;
    };

    bmiStatus(bmi);
}