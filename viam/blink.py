import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.board import Board


async def connect():
    opts = RobotClient.Options.with_api_key(
        # Replace "<API-KEY>" (including brackets) with your machine's API key
        api_key='igtr7ihual0wm9zghvt18fxi177lhr5w',
        # Replace "<API-KEY-ID>" (including brackets) with your machine's
        # API key ID
        api_key_id='7c22382a-aace-47e9-a53c-0c24b2d6889a'
    )
    return await RobotClient.at_address("airobot-main.8f5d3ntpt7.viam.cloud", opts)

async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)

    local = Board.from_robot(robot, 'Raspberry-Pi-5')
    led = await local.gpio_pin_by_name('38')

    while (True):
        # When True, sets the LED pin to high or on.
        await led.set(True)
        print('LED is on')
        await asyncio.sleep(1)

        # When False, sets the pin to low or off.
        await led.set(False)
        print('LED is off')
        await asyncio.sleep(1)

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
