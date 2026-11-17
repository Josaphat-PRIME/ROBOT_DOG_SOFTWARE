from gpiozero import AngularServo
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Configuration du GPIO
GPIO_SERVO = 18

# Initialisation du servo
factory = LGPIOFactory(chip=0)

servo = AngularServo(
    GPIO_SERVO,
    min_angle=0,
    max_angle=180,
    min_pulse_width=0.0006,
    max_pulse_width=0.0024,
    frame_width=0.020,
    pin_factory=factory
)


def set_angle(angle):
    """Positionne le servo à un angle donné."""

    angle = max(10, min(170, angle))

    servo.angle = angle

    print(f"Position du servo : {angle}°")


def move_smooth(target, duration=1.0):
    """Déplacement progressif vers une position."""

    start = servo.angle

    if start is None:
        start = 90

    steps = 50

    for i in range(steps + 1):

        ratio = i / steps

        angle = start + (target - start) * ratio

        servo.angle = angle

        sleep(duration / steps)

    print(f"Position atteinte : {target}°")


def main():

    print("\n===== MG90 SERVO CONTROL =====")
    print("1 - Position 0°")
    print("2 - Position 45°")
    print("3 - Position 90°")
    print("4 - Position 135°")
    print("5 - Position 180°")
    print("6 - Angle personnalisé")
    print("7 - Déplacement progressif")
    print("0 - Quitter")

    try:
        while True:

            choice = input("\nVotre choix : ")

            if choice == "1":
                set_angle(10)

            elif choice == "2":
                set_angle(45)

            elif choice == "3":
                set_angle(90)

            elif choice == "4":
                set_angle(135)

            elif choice == "5":
                set_angle(170)

            elif choice == "6":
                angle = float(input("Angle souhaité : "))
                set_angle(angle)

            elif choice == "7":
                angle = float(input("Angle final : "))
                duration = float(input("Durée (secondes) : "))
                move_smooth(angle, duration)

            elif choice == "0":
                break

            else:
                print("Choix invalide.")

    except KeyboardInterrupt:
        print("\nArrêt du programme.")

    finally:
        servo.detach()
        factory.close()


if __name__ == "__main__":
    main()