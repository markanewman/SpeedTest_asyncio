import asyncio
import aiofiles
import pathlib
from argparse import ArgumentParser

async def copy_file(source: pathlib.Path, dest: pathlib.Path) -> None:
    async with aiofiles.open(source, "r", encoding = 'utf8') as fp_1:
        async with aiofiles.open(dest, "w", encoding = 'utf8') as fp_2:
            async for line in fp_1:
                await fp_2.write(line)

async def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-source', type = pathlib.Path)
    parser.add_argument('-dest', type = pathlib.Path)
    args = parser.parse_args()
    await copy_file(args.source, args.dest)

if __name__ == "__main__":    
    asyncio.run(main())
