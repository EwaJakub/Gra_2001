# Gra_2001

Warsztat: Salon gier (*)

Zaimplementuj grę 2001. Poniżej znajdziesz zasady.
2001 – Zasady Gry

1. Każdy z graczy zaczyna z liczbą punktów równą 0.
2. W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
3. Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów. 
4. Począwszy od drugiej tury:
   * jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową, 
   * jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
5. Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.

Implementacja

* Zaimplementuj grę w wersji dla dwóch graczy. 
* Niech będzie to aplikacja konsolowa. 
* Niech drugim graczem będzie komputer. 
* Po każdej turze wyświetl aktualną liczbę punktów. 
* Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter. Rzut komputera następuje 
automatycznie, po rzucie gracza. Zakończ program w momencie, gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.

Modyfikacja 1

Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko i wyłącznie, 
do klikania klawisza enter. Spróbujmy uczynić ją trochę bardziej interaktywną.

* Przed każdym rzutem, daj graczowi wybór. 
* Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100. 
* Kości mogą się powtarzać, gracz może też użyć 2 różnych kości. 
* Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego 
łańcucha znaków przez gracza 
(po jednym na każdą z kości). 
* Możesz wykorzystać kod z zadania Kostka do gry. 
* Wybór kości przez komputer niech będzie losowy.

Reszta zasad pozostaje bez zmian.

Modyfikacja 2

Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. Aby przechowywać informację między turami, 
wykorzystaj ukryte pola formularza. Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie), 
ale na tę chwilę się tym nie przejmujemy. Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.
