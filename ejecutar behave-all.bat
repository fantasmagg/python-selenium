echo. ################## pruevas ##################

echo. ############### xml and behave ##############
echo. behave --junit --tags--skip --no-skipped

cd .\src\
echo. ##################### ELIMINAR CARPETA CARPETA DE RESULTADOS ##################
echo. del /f /q .\allure-results

echo. behave -f allure_behave.formatter:AllureFormatter --tags-probandoElCambioDeVentanas--tags--skip --no-skipped -o .\allure-results ./features -f pretty

behave -f allure_behave.formatter:AllureFormatter -o .\allure-results -f pretty
pause