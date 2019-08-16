import collections

class Solution:
    def __init__(self):
        self.explicit, self.installed = set(), set()
        self.pgm_to_deps, self.dep_to_pgms = collections.defaultdict(set), collections.defaultdict(set)

    def install(self, program):
        # Check if already installed
        if program in self.installed:
            print(f"{program} is already installed")
            return

        self.explicit.add(program)
        self.dfs_install(program)

    def dfs_install(self, program):
        if program in self.installed: return

        for req in self.pgm_to_deps[program]:
            self.dfs_install(req)

        self.installed.add(program)
        print(f"Installing {program}")

    def remove(self, program):
        # Check if already installed
        if program not in self.installed:
            print(f"{program} is not installed")
            return

        # Can't remove if this program
        if self.dep_to_pgms[program]:
            print(f'{program} is still needed')
            return

        print(f'Removing {program}')
        self.installed.remove(program)
        self.explicit.remove(program)

        for dep in self.pgm_to_deps[program]:
            self.dfs_remove(dep)

    def dfs_remove(self, program):
        if self.dep_to_pgms[program]&self.installed or program in self.explicit: return
        self.installed.remove(program)
        print(f'Removing {program}')

        for nbr in self.pgm_to_deps[program]:
            self.dfs_remove(nbr)

    def list_programs(self):
        for p in self.installed:
            print(p)

    def add_deps(self, program, deps):
        if not self.valid_dependency(program, deps): return False

        for dep in deps:
            self.pgm_to_deps[program].add(dep)
            self.dep_to_pgms[dep].add(program)

    def valid_dependency(self, program, deps):
        for p in deps:
            if program in self.pgm_to_deps[p]:
                print(f"{p} depends on {program}, ignoring command")
                return False

        return True

    def handle_input(self):
        n = int(input())
        for _ in range(n):
            full_cmd = input()
            print(full_cmd)
            cmd = full_cmd.split()
            cmd = list(map(str.strip, cmd))

            if cmd[0] == 'DEPEND':
                self.add_deps(cmd[1], cmd[2:])
            elif cmd[0] == 'INSTALL':
                self.install(cmd[1])
            elif cmd[0] == 'REMOVE':
                self.remove(cmd[1])
            elif cmd[0] == 'LIST':
                self.list_programs()
            elif cmd[0] == 'END':
                return

if __name__ == "__main__":
    sol = Solution()
    sol.handle_input()
