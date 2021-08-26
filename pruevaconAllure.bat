echo.############################ TEST PATH ###########################
cd .\src\test
python -m pytest schenchot_para_allure.py --alluredir ..\allure-results
python -m pytest scheschot.py --alluredir ..\allure-results
pause