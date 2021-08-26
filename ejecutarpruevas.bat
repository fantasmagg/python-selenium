echo.############################ TEST PATH ###########################
cd .\src\test
python -m pytest usandoExecl.py scheschot.py --junit-xml=../results/results.xml
pause