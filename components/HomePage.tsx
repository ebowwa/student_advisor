/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/Tp6GzZ8XmmC
 */
import Link from "next/link"

export function HomePage() {
  return (
    <>
      <div className="bg-gray-50/90 py-12 lg:py-24">
        <div className="container px-4 md:px-6">
          <div className="grid max-w-3xl gap-4 mx-auto items-start space-y-4 lg:gap-10 lg:flex lg:items-center lg:space-y-0">
            <div className="space-y-2 text-center lg:text-left">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl">Assist.org API</h1>
              <p className="text-gray-500 dark:text-gray-400">
                Provides data and functionality for the assist.org website.
              </p>
            </div>
            <div className="flex flex-col gap-2 min-[400px]:flex-row justify-center lg:justify-end">
              <Link
                className="inline-flex h-10 items-center justify-center rounded-md border border-gray-200 bg-white px-8 text-sm font-medium shadow-sm gap-1 transition-colors hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300 dark:border-gray-800"
                href="#"
              >
                Back to assist.org
              </Link>
              <Link
                className="inline-flex h-10 items-center justify-center rounded-md bg-gray-900 px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                href="#"
              >
                Documentation
              </Link>
            </div>
          </div>
        </div>
      </div>
      <section className="container py-12 md:py-24 lg:py-32">
        <div className="grid max-w-3xl gap-4 mx-auto items-start space-y-4 lg:gap-10 lg:flex lg:items-center lg:space-y-0">
          <div className="space-y-2 text-center lg:text-left">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Endpoints</h2>
            <p className="text-gray-500 dark:text-gray-400">
              Available API endpoints with a brief description of their purpose.
            </p>
          </div>
          <div className="space-y-4">
            <div>
              <h3 className="font-bold">/courses</h3>
              <p>Retrieve course data.</p>
            </div>
            <div>
              <h3 className="font-bold">/majors</h3>
              <p>Retrieve major data.</p>
            </div>
            <div>
              <h3 className="font-bold">/institutions</h3>
              <p>Retrieve institution data.</p>
            </div>
          </div>
        </div>
      </section>
      <section className="container py-12 md:py-24 lg:py-32">
        <div className="grid max-w-3xl gap-4 mx-auto items-start space-y-4 lg:gap-10 lg:flex lg:items-center lg:space-y-0">
          <div className="space-y-2 text-center lg:text-left">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Authentication</h2>
            <p className="text-gray-500 dark:text-gray-400">
              The Assist.org API requires an API key for authentication. To obtain an API key, please contact our
              support team.
            </p>
          </div>
        </div>
      </section>
      <footer className="border-t">
        <div className="container flex flex-col gap-4 py-12 md:py-24 lg:py-32 px-4 md:px-6">
          <nav className="flex flex-col gap-2 md:flex-row md:gap-4 lg:gap-0 lg:space-x-4 xl:space-x-6">
            <Link
              className="inline-flex h-8 items-center rounded-lg px-3 text-sm font-medium text-gray-900 hover:text-gray-900 dark:text-gray-50 dark:hover:text-gray-50"
              href="#"
            >
              Home
            </Link>
            <Link
              className="inline-flex h-8 items-center rounded-lg px-3 text-sm font-medium text-gray-900 hover:text-gray-900 dark:text-gray-50 dark:hover:text-gray-50"
              href="#"
            >
              API
            </Link>
            <Link
              className="inline-flex h-8 items-center rounded-lg px-3 text-sm font-medium text-gray-900 hover:text-gray-900 dark:text-gray-50 dark:hover:text-gray-50"
              href="#"
            >
              Documentation
            </Link>
            <Link
              className="inline-flex h-8 items-center rounded-lg px-3 text-sm font-medium text-gray-900 hover:text-gray-900 dark:text-gray-50 dark:hover:text-gray-50"
              href="#"
            >
              Support
            </Link>
          </nav>
        </div>
      </footer>
    </>
  )
}