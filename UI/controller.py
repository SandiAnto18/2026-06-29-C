import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        # ATTENZIONE ARRIVA UNA LISTA DA MODEL.PY
        # e per il numero di nodi devo stampare un numero quindi uso len
        self._model.buildGraph()
        # devo costruire il grafo
        self._view._txt_result.controls.clear()
        # comando per aggiungere righe testuali/numero in output
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi:{self._model.getNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi:{self._model.getEdges()}"))

        self._view.update_page()

    def handleStampaInfo(self,e):

            # PULISCO L'AREA DEI RISULTATI
            self._view._txt_result.controls.clear()

            # ARTISTA CON GRADO MAGGIORE
            artistDegree,grado = self._model.getArtistMaxDegree()
            self._view._txt_result.controls.append(
                ft.Text(f"ARTISTA CON GRADO MAGGIORE: {artistDegree} (grado: {grado})")

            )

            # ARTISTA CON SOMMA DEI PESI INCIDENTI MASSIMA
            artistWeight,somma = self._model.getArtistMaxWeight()

            self._view._txt_result.controls.append(
                ft.Text(f"ARTISTA CON SOMMA DEI PESI INCIDENTI MASSIMA: {artistWeight}(somma:{somma})")
            )

            # TOP 10 ARCHI DI PESO MAGGIORE
            topEdges = self._model.getTop10Edges()
            self._view._txt_result.controls.append(
                ft.Text("TOP 10 ARCHI DI PESO MAGGIORE:")
            )

            # STAMPO I 10 ARCHI senza numerazione(1. ... 2. ...)
            #for artist1, artist2, data in topEdges:
            #    self._view._txt_result.controls.append(
            #        ft.Text(f"{artist1} -- {artist2} (peso: {data["weight"]})")
            #    )
            # STAMPO I 10 ARCHI con numerazione
            for i, (artist1, artist2, data) in enumerate(topEdges, start=1):
                self._view._txt_result.controls.append(
                    ft.Text(f"{i}. {artist1} -- {artist2}: (peso = {data['weight']})")
                )

            self._view.update_page()

    def handleSelezione(self,e):
        pass