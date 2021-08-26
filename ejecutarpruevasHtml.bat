echo.############################ TEST PATH ###########################
cd .\src\test
python -m pytest usandoExecl.py scheschot.py --html=../results/results.html --self-contained-html
pause