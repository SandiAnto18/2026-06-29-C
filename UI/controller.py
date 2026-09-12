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
        pass

    def handleSelezione(self,e):
        pass