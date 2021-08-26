@Selenium
# Created by saitama at 22/8/2021
Feature: Funciones basicas de selenium BDD
  # Enter feature description here

  Scenario: abri el navegaro
     Given open brower
     Then DOM Spotify_mensajedeError
     And escribir email Emailsing texto: hola
     And selecinar mes por texto elemento : select_month mes Febrero
     And select value select_month y 01
     And captura de pantalla spoti
     And guardar ventana : spoti
     And ir a otra ventana url : https://www.google.com/
     And guardar ventana : google
     And guardar ventana : spoti



  @Probando
  Scenario: probando cambio de ventanas
     Given open brower
     Then DOM Spotify_mensajedeError
     And guardar ventana : spoti
     And ir a otra ventana url : https://www.google.com/
     And guardar ventana : google
     And guardar ventana : spoti
     And escribir email Emailsing texto: hola
     And selecinar mes por texto elemento : select_month mes Febrero
     And captura de pantalla spoti